<script lang="ts">
    import { onMount } from "svelte";

    interface Game {
        id: number;
        title: string;
        description: string;
        publisher?: { id: number; name: string };
        category?: { id: number; name: string };
        publisher_name?: string;
        category_name?: string;
    }

    interface FilterOption {
        id: number;
        name: string;
    }

    export let games: Game[] = [];
    let loading = true;
    let error: string | null = null;
    
    // Filter state
    let categories: FilterOption[] = [];
    let publishers: FilterOption[] = [];
    let selectedCategoryId: number | null = null;
    let selectedPublisherId: number | null = null;

    /**
     * Build the API URL with filter query parameters.
     * @returns The API URL with optional category_id and publisher_id parameters.
     */
    const buildApiUrl = (): string => {
        const params = new URLSearchParams();
        if (selectedCategoryId !== null) {
            params.set('category_id', selectedCategoryId.toString());
        }
        if (selectedPublisherId !== null) {
            params.set('publisher_id', selectedPublisherId.toString());
        }
        const queryString = params.toString();
        return queryString ? `/api/games?${queryString}` : '/api/games';
    };

    /**
     * Update the browser URL to reflect current filter state.
     */
    const updateBrowserUrl = (): void => {
        const params = new URLSearchParams();
        if (selectedCategoryId !== null) {
            params.set('category', selectedCategoryId.toString());
        }
        if (selectedPublisherId !== null) {
            params.set('publisher', selectedPublisherId.toString());
        }
        const queryString = params.toString();
        const newUrl = queryString ? `?${queryString}` : window.location.pathname;
        window.history.replaceState({}, '', newUrl);
    };

    /**
     * Read filter parameters from the current URL.
     */
    const readUrlParams = (): void => {
        const params = new URLSearchParams(window.location.search);
        const categoryParam = params.get('category');
        const publisherParam = params.get('publisher');
        
        if (categoryParam) {
            selectedCategoryId = parseInt(categoryParam, 10);
        }
        if (publisherParam) {
            selectedPublisherId = parseInt(publisherParam, 10);
        }
    };

    const fetchGames = async () => {
        loading = true;
        try {
            const response = await fetch(buildApiUrl());
            if(response.ok) {
                games = await response.json();
            } else {
                error = `Failed to fetch data: ${response.status} ${response.statusText}`;
            }
        } catch (err) {
            error = `Error: ${err instanceof Error ? err.message : String(err)}`;
        } finally {
            loading = false;
        }
    };

    const fetchCategories = async () => {
        try {
            const response = await fetch('/api/categories/');
            if (response.ok) {
                categories = await response.json();
            }
        } catch (err) {
            console.error('Failed to fetch categories:', err);
        }
    };

    const fetchPublishers = async () => {
        try {
            const response = await fetch('/api/publishers/');
            if (response.ok) {
                publishers = await response.json();
            }
        } catch (err) {
            console.error('Failed to fetch publishers:', err);
        }
    };

    /**
     * Handle filter changes and refresh the game list.
     */
    const handleFilterChange = (): void => {
        updateBrowserUrl();
        fetchGames();
    };

    /**
     * Clear all active filters and refresh the game list.
     */
    const clearFilters = (): void => {
        selectedCategoryId = null;
        selectedPublisherId = null;
        updateBrowserUrl();
        fetchGames();
    };

    $: hasActiveFilters = selectedCategoryId !== null || selectedPublisherId !== null;

    onMount(() => {
        readUrlParams();
        fetchCategories();
        fetchPublishers();
        fetchGames();
    });
</script>

<div>
    <h2 class="text-2xl font-medium mb-6 text-slate-100">Featured Games</h2>
    
    <!-- Filter Controls -->
    <div class="mb-6 p-4 bg-slate-800/60 backdrop-blur-sm rounded-xl border border-slate-700/50" data-testid="filter-controls">
        <div class="flex flex-wrap items-center gap-4">
            <!-- Category Filter -->
            <div class="flex flex-col sm:flex-row sm:items-center gap-2">
                <label for="category-filter" class="text-sm font-medium text-slate-300">Category:</label>
                <select 
                    id="category-filter"
                    bind:value={selectedCategoryId}
                    on:change={handleFilterChange}
                    class="bg-slate-700 text-slate-100 text-sm rounded-lg border border-slate-600 focus:ring-blue-500 focus:border-blue-500 px-3 py-2 min-w-[150px]"
                    data-testid="category-filter"
                >
                    <option value={null}>All Categories</option>
                    {#each categories as category}
                        <option value={category.id}>{category.name}</option>
                    {/each}
                </select>
            </div>
            
            <!-- Publisher Filter -->
            <div class="flex flex-col sm:flex-row sm:items-center gap-2">
                <label for="publisher-filter" class="text-sm font-medium text-slate-300">Publisher:</label>
                <select 
                    id="publisher-filter"
                    bind:value={selectedPublisherId}
                    on:change={handleFilterChange}
                    class="bg-slate-700 text-slate-100 text-sm rounded-lg border border-slate-600 focus:ring-blue-500 focus:border-blue-500 px-3 py-2 min-w-[150px]"
                    data-testid="publisher-filter"
                >
                    <option value={null}>All Publishers</option>
                    {#each publishers as publisher}
                        <option value={publisher.id}>{publisher.name}</option>
                    {/each}
                </select>
            </div>
            
            <!-- Clear Filters Button -->
            {#if hasActiveFilters}
                <button 
                    on:click={clearFilters}
                    class="text-sm font-medium text-blue-400 hover:text-blue-300 transition-colors flex items-center gap-1"
                    data-testid="clear-filters"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                    Clear filters
                </button>
            {/if}
        </div>
    </div>
    
    {#if loading}
        <!-- loading animation -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {#each Array(6) as _, i}
                <div class="bg-slate-800/60 backdrop-blur-sm rounded-xl overflow-hidden shadow-lg border border-slate-700/50">
                    <div class="p-6">
                        <div class="animate-pulse">
                            <div class="h-6 bg-slate-700 rounded w-3/4 mb-3"></div>
                            <div class="h-4 bg-slate-700 rounded w-1/2 mb-4"></div>
                            <div class="h-3 bg-slate-700 rounded w-full mb-3"></div>
                            <div class="h-3 bg-slate-700 rounded w-5/6 mb-4"></div>
                            <div class="h-2 bg-slate-700 rounded-full w-full mb-2"></div>
                            <div class="h-4 bg-slate-700 rounded w-1/4 mt-4"></div>
                        </div>
                    </div>
                </div>
            {/each}
        </div>
    {:else if error}
        <!-- error display -->
        <div class="text-center py-12 bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700">
            <p class="text-red-400">{error}</p>
        </div>
    {:else if games.length === 0}
        <!-- no games found -->
        <div class="text-center py-12 bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700">
            <p class="text-slate-300">No games available at the moment.</p>
        </div>
    {:else}
        <!-- game list -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6" data-testid="games-grid">
            {#each games as game (game.id)}
                <a 
                    href={`/game/${game.id}`} 
                    class="group block bg-slate-800/60 backdrop-blur-sm rounded-xl overflow-hidden shadow-lg border border-slate-700/50 hover:border-blue-500/50 hover:shadow-blue-500/10 hover:shadow-xl transition-all duration-300 hover:translate-y-[-6px]"
                    data-testid="game-card"
                    data-game-id={game.id}
                    data-game-title={game.title}
                >
                    <div class="p-6 relative">
                        <div class="absolute inset-0 bg-gradient-to-r from-blue-600/10 to-purple-600/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                        <div class="relative z-10">
                            <h3 class="text-xl font-semibold text-slate-100 mb-2 group-hover:text-blue-400 transition-colors" data-testid="game-title">{game.title}</h3>
                            
                            {#if game.category?.name || game.publisher?.name}
                                <div class="flex gap-2 mb-3">
                                    {#if game.category?.name}
                                        <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-blue-900/60 text-blue-300" data-testid="game-category">
                                            {game.category.name}
                                        </span>
                                    {/if}
                                    {#if game.publisher?.name}
                                        <span class="text-xs font-medium px-2.5 py-0.5 rounded bg-purple-900/60 text-purple-300" data-testid="game-publisher">
                                            {game.publisher.name}
                                        </span>
                                    {/if}
                                </div>
                            {/if}
                            
                            <p class="text-slate-400 mb-4 text-sm line-clamp-2" data-testid="game-description">{game.description}</p>
                            
                            <div class="mt-4 text-sm text-blue-400 font-medium flex items-center">
                                <span>View details</span>
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 ml-1 transform transition-transform duration-300 group-hover:translate-x-2" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                                </svg>
                            </div>
                        </div>
                    </div>
                </a>
            {/each}
        </div>
    {/if}
</div>