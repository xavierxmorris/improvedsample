# Tailspin Toys Crowd Funding Platform

This is a crowdfunding platform for games with a developer theme. The application enables game publishers to create campaigns and backers to support game development.

## Project Overview

- **Purpose:** Allow game developers to crowdfund their projects
- **Target Users:** Game developers (publishers) and gaming enthusiasts (backers)
- **Key Features:** Game listings, campaign management, backer pledges, category browsing

## Technology Stack

### Backend
- Python 3.11+ with Flask framework
- SQLAlchemy ORM for database interactions
- SQLite for development, PostgreSQL for production
- RESTful API design patterns

### Frontend
- Astro for page routing and static content
- Svelte for interactive components
- Tailwind CSS for styling
- TypeScript for type safety

## Folder Structure

- `/server`: Flask backend API
  - `/models`: SQLAlchemy ORM models
  - `/routes`: API endpoints organized by resource
  - `/tests`: Unit tests for the API
  - `/utils`: Utility functions and helpers
- `/client`: Astro/Svelte frontend
  - `/src/components`: Reusable Svelte components
  - `/src/layouts`: Astro layout templates
  - `/src/pages`: Astro page routes
  - `/src/styles`: CSS and Tailwind configuration
- `/scripts`: Development and deployment scripts
- `/data`: Database files
- `/docs`: Project documentation

## Coding Standards

### Python
- Use type hints for all function parameters and return values
- Include docstrings for all functions and classes
- Follow PEP 8 style guidelines
- Use SQLAlchemy models for all database operations

### TypeScript/JavaScript
- Use TypeScript for all new code
- Prefer `const` over `let`, avoid `var`
- Use arrow functions for callbacks
- Export types and interfaces explicitly

### General
- Add a comment block at the top of each file explaining its purpose
- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Write tests for all new functionality

## UI Guidelines

- Maintain dark mode theme throughout the application
- Use rounded corners for UI elements (rounded-lg or rounded-xl)
- Follow accessible design patterns (proper contrast, focus states)
- Use Tailwind CSS utility classes exclusively

## Scripts

Use existing scripts rather than manual commands:
- `scripts/setup-env.sh`: Install all dependencies
- `scripts/run-server-tests.sh`: Run Python tests
- `scripts/start-app.sh`: Start both backend and frontend
