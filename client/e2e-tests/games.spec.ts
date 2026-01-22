import { test, expect } from '@playwright/test';

test.describe('Game Listing and Navigation', () => {
  test('should display games with titles on index page', async ({ page }) => {
    await page.goto('/');
    
    // Wait for the games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Check that games are displayed
    const gameCards = page.locator('[data-testid="game-card"]');
    
    // Wait for at least one game card to be visible
    await expect(gameCards.first()).toBeVisible();
    
    // Check that we have at least one game
    const gameCount = await gameCards.count();
    expect(gameCount).toBeGreaterThan(0);
    
    // Check that each game card has a title
    const firstGameCard = gameCards.first();
    await expect(firstGameCard.locator('[data-testid="game-title"]')).toBeVisible();
    
    // Verify that game titles are not empty
    const gameTitle = await firstGameCard.locator('[data-testid="game-title"]').textContent();
    expect(gameTitle?.trim()).toBeTruthy();
  });

  test('should navigate to correct game details page when clicking on a game', async ({ page }) => {
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Get the first game card and its data attributes
    const firstGameCard = page.locator('[data-testid="game-card"]').first();
    const gameId = await firstGameCard.getAttribute('data-game-id');
    const gameTitle = await firstGameCard.getAttribute('data-game-title');
    
    // Click on the first game
    await firstGameCard.click();
    
    // Verify we're on the correct game details page
    await expect(page).toHaveURL(`/game/${gameId}`);
    
    // Verify the game details page loads
    await page.waitForSelector('[data-testid="game-details"]', { timeout: 10000 });
    
    // Verify the title matches what we clicked on
    const detailsTitle = page.locator('[data-testid="game-details-title"]');
    await expect(detailsTitle).toHaveText(gameTitle || '');
  });

  test('should display game details with all required information', async ({ page }) => {
    // Navigate to a specific game (we'll use game ID 1 as an example)
    await page.goto('/game/1');
    
    // Wait for game details to load
    await page.waitForSelector('[data-testid="game-details"]', { timeout: 10000 });
    
    // Check that the game title is present and not empty
    const gameTitle = page.locator('[data-testid="game-details-title"]');
    await expect(gameTitle).toBeVisible();
    const titleText = await gameTitle.textContent();
    expect(titleText?.trim()).toBeTruthy();
    
    // Check that the game description is present and not empty
    const gameDescription = page.locator('[data-testid="game-details-description"]');
    await expect(gameDescription).toBeVisible();
    const descriptionText = await gameDescription.textContent();
    expect(descriptionText?.trim()).toBeTruthy();
    
    // Check that either publisher or category (or both) are present
    const publisherExists = await page.locator('[data-testid="game-details-publisher"]').isVisible();
    const categoryExists = await page.locator('[data-testid="game-details-category"]').isVisible();
    expect(publisherExists && categoryExists).toBeTruthy();
    
    // If publisher exists, check it has content
    if (publisherExists) {
      const publisherText = await page.locator('[data-testid="game-details-publisher"]').textContent();
      expect(publisherText?.trim()).toBeTruthy();
    }
    
    // If category exists, check it has content
    if (categoryExists) {
      const categoryText = await page.locator('[data-testid="game-details-category"]').textContent();
      expect(categoryText?.trim()).toBeTruthy();
    }
  });

  test('should display a button to back the game', async ({ page }) => {
    await page.goto('/game/1');
    
    // Wait for game details to load
    await page.waitForSelector('[data-testid="game-details"]', { timeout: 10000 });
    
    // Check that the back game button is present
    const backButton = page.locator('[data-testid="back-game-button"]');
    await expect(backButton).toBeVisible();
    await expect(backButton).toContainText('Support This Game');
    
    // Verify the button is clickable
    await expect(backButton).toBeEnabled();
  });

  test('should be able to navigate back to home from game details', async ({ page }) => {
    await page.goto('/game/1');
    
    // Wait for the page to load
    await page.waitForSelector('[data-testid="game-details"]', { timeout: 10000 });
    
    // Find and click the back to all games link
    const backLink = page.locator('a:has-text("Back to all games")');
    await expect(backLink).toBeVisible();
    await backLink.click();
    
    // Verify we're back on the home page
    await expect(page).toHaveURL('/');
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
  });

  test('should handle navigation to non-existent game gracefully', async ({ page }) => {
    // Navigate to a game that doesn't exist
    await page.goto('/game/99999');
    
    // The page should load without crashing
    // Check if there's an error message or if it handles gracefully
    await page.waitForTimeout(3000);
    
    // The page should either show an error or handle it gracefully
    // We expect the page to not crash and still have a valid title
    await expect(page).toHaveTitle(/Game Details - Tailspin Toys/);
  });
});

test.describe('Game Filtering', () => {
  test('should display filter controls on home page', async ({ page }) => {
    await page.goto('/');
    
    // Wait for the page to load
    await page.waitForSelector('[data-testid="filter-controls"]', { timeout: 10000 });
    
    // Check that filter controls are visible
    const filterControls = page.locator('[data-testid="filter-controls"]');
    await expect(filterControls).toBeVisible();
    
    // Check that category filter dropdown exists
    const categoryFilter = page.locator('[data-testid="category-filter"]');
    await expect(categoryFilter).toBeVisible();
    
    // Check that publisher filter dropdown exists
    const publisherFilter = page.locator('[data-testid="publisher-filter"]');
    await expect(publisherFilter).toBeVisible();
  });

  test('should filter games by category', async ({ page }) => {
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Get initial game count
    const initialGameCards = page.locator('[data-testid="game-card"]');
    const initialCount = await initialGameCards.count();
    expect(initialCount).toBeGreaterThan(0);
    
    // Select a category from the dropdown
    const categoryFilter = page.locator('[data-testid="category-filter"]');
    await categoryFilter.selectOption({ index: 1 }); // Select first non-default option
    
    // Wait for the games to reload
    await page.waitForTimeout(500);
    
    // Verify that URL contains the category filter parameter
    await expect(page).toHaveURL(/category=/);
  });

  test('should filter games by publisher', async ({ page }) => {
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Select a publisher from the dropdown
    const publisherFilter = page.locator('[data-testid="publisher-filter"]');
    await publisherFilter.selectOption({ index: 1 }); // Select first non-default option
    
    // Wait for the games to reload
    await page.waitForTimeout(500);
    
    // Verify that URL contains the publisher filter parameter
    await expect(page).toHaveURL(/publisher=/);
  });

  test('should filter games by both category and publisher', async ({ page }) => {
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Select a category
    const categoryFilter = page.locator('[data-testid="category-filter"]');
    await categoryFilter.selectOption({ index: 1 });
    
    // Wait for the games to reload
    await page.waitForTimeout(500);
    
    // Select a publisher
    const publisherFilter = page.locator('[data-testid="publisher-filter"]');
    await publisherFilter.selectOption({ index: 1 });
    
    // Wait for the games to reload
    await page.waitForTimeout(500);
    
    // Verify that URL contains both filter parameters
    await expect(page).toHaveURL(/category=/);
    await expect(page).toHaveURL(/publisher=/);
  });

  test('should show clear filters button when filters are active', async ({ page }) => {
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Clear filters button should not be visible initially
    const clearButton = page.locator('[data-testid="clear-filters"]');
    await expect(clearButton).not.toBeVisible();
    
    // Select a category to activate a filter
    const categoryFilter = page.locator('[data-testid="category-filter"]');
    await categoryFilter.selectOption({ index: 1 });
    
    // Wait for the games to reload
    await page.waitForTimeout(500);
    
    // Clear filters button should now be visible
    await expect(clearButton).toBeVisible();
  });

  test('should clear all filters when clicking clear button', async ({ page }) => {
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Apply filters
    const categoryFilter = page.locator('[data-testid="category-filter"]');
    await categoryFilter.selectOption({ index: 1 });
    await page.waitForTimeout(500);
    
    const publisherFilter = page.locator('[data-testid="publisher-filter"]');
    await publisherFilter.selectOption({ index: 1 });
    await page.waitForTimeout(500);
    
    // Click clear filters button
    const clearButton = page.locator('[data-testid="clear-filters"]');
    await clearButton.click();
    
    // Wait for the page to update
    await page.waitForTimeout(500);
    
    // Verify URL no longer has filter parameters
    const url = page.url();
    expect(url).not.toContain('category=');
    expect(url).not.toContain('publisher=');
    
    // Clear button should no longer be visible
    await expect(clearButton).not.toBeVisible();
  });

  test('should preserve filters in URL for bookmarking', async ({ page }) => {
    await page.goto('/');
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Apply a category filter
    const categoryFilter = page.locator('[data-testid="category-filter"]');
    await categoryFilter.selectOption({ index: 1 });
    await page.waitForTimeout(500);
    
    // Get the current URL with filter
    const filteredUrl = page.url();
    expect(filteredUrl).toContain('category=');
    
    // Navigate away and back using the filtered URL
    await page.goto('/about');
    await page.goto(filteredUrl);
    
    // Wait for games to load
    await page.waitForSelector('[data-testid="games-grid"]', { timeout: 10000 });
    
    // Verify the filter is still applied (URL should still have the parameter)
    await expect(page).toHaveURL(/category=/);
  });
});
