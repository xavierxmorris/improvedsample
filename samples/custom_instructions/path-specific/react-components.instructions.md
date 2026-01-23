# Svelte Component Instructions

These instructions apply to all Svelte component files.

---
applyTo: "**/*.svelte"
---

## Component Structure

- Use TypeScript in `<script lang="ts">` blocks
- Define props using `export let` with type annotations
- Keep components focused on a single responsibility

## Styling

- Use Tailwind CSS utility classes exclusively
- Follow dark mode theme (dark backgrounds, light text)
- Use consistent spacing: `p-4`, `m-2`, `gap-4`
- Apply rounded corners: `rounded-lg` or `rounded-xl`

## Accessibility

- Include proper ARIA labels for interactive elements
- Ensure sufficient color contrast
- Add focus states for keyboard navigation
- Use semantic HTML elements

## State Management

- Use Svelte's reactive declarations (`$:`) for derived state
- Keep component state minimal and local
- Use stores for shared state across components

## Example Component

```svelte
<script lang="ts">
  /** Props for the GameCard component */
  export let title: string;
  export let description: string;
  export let fundingGoal: number;
  export let currentFunding: number;

  /** Calculate funding progress percentage */
  $: progress = Math.min((currentFunding / fundingGoal) * 100, 100);
</script>

<article class="bg-gray-800 rounded-xl p-4 shadow-lg">
  <h3 class="text-xl font-bold text-white">{title}</h3>
  <p class="text-gray-300 mt-2">{description}</p>
  <div class="mt-4">
    <div class="bg-gray-700 rounded-full h-2">
      <div 
        class="bg-green-500 rounded-full h-2" 
        style="width: {progress}%"
        role="progressbar"
        aria-valuenow={progress}
        aria-valuemin={0}
        aria-valuemax={100}
      />
    </div>
  </div>
</article>
```
