# New Svelte Component

Your goal is to generate a new Svelte component following project conventions.

## Required Information

Ask for the following if not provided:
- Component name and purpose
- Props the component needs
- Whether it needs state management
- Any API data it should fetch

## Component Requirements

### File Location

Create in `client/src/components/{ComponentName}.svelte`

### TypeScript

- Use `<script lang="ts">` for type safety
- Define types for all props
- Export prop types if they may be reused

### Styling with Tailwind

- Use Tailwind utility classes exclusively
- Follow dark mode theme:
  - Backgrounds: `bg-gray-800`, `bg-gray-900`
  - Text: `text-white`, `text-gray-300`
  - Accents: `text-blue-400`, `bg-green-500`
- Apply consistent spacing and rounded corners

### Accessibility

- Use semantic HTML elements
- Include ARIA labels for interactive elements
- Ensure keyboard navigation works
- Maintain proper heading hierarchy

## Component Template

```svelte
<script lang="ts">
  /**
   * {ComponentName} - {Brief description}
   *
   * @component
   * @example
   * <{ComponentName} prop={value} />
   */

  // Props
  export let requiredProp: string;
  export let optionalProp: string = "default";

  // Local state
  let isLoading = false;

  // Reactive declarations
  $: derivedValue = computeValue(requiredProp);

  // Functions
  function handleClick(): void {
    // Handle interaction
  }
</script>

<div class="bg-gray-800 rounded-xl p-4 shadow-lg">
  <h2 class="text-xl font-bold text-white mb-4">
    {requiredProp}
  </h2>
  
  {#if isLoading}
    <div class="flex justify-center">
      <span class="text-gray-400">Loading...</span>
    </div>
  {:else}
    <div class="text-gray-300">
      <!-- Component content -->
    </div>
  {/if}
  
  <button
    on:click={handleClick}
    class="mt-4 px-4 py-2 bg-blue-600 hover:bg-blue-700 
           text-white rounded-lg transition-colors
           focus:outline-none focus:ring-2 focus:ring-blue-500"
  >
    Action
  </button>
</div>

<style>
  /* Only use for styles not achievable with Tailwind */
</style>
```

## Common Patterns

### Fetching Data

```svelte
<script lang="ts">
  import { onMount } from "svelte";

  let data: GameData[] = [];
  let error: string | null = null;

  onMount(async () => {
    try {
      const response = await fetch("/api/games");
      data = await response.json();
    } catch (e) {
      error = "Failed to load data";
    }
  });
</script>
```

### Event Dispatching

```svelte
<script lang="ts">
  import { createEventDispatcher } from "svelte";
  
  const dispatch = createEventDispatcher<{
    select: { id: number };
    close: void;
  }>();

  function handleSelect(id: number): void {
    dispatch("select", { id });
  }
</script>
```

### Slots for Composition

```svelte
<div class="card">
  <slot name="header" />
  <slot />
  <slot name="footer" />
</div>
```
