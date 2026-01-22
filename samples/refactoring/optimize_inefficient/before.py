"""
Before: Inefficient Python code with performance issues.

This module demonstrates common performance anti-patterns that Copilot
can help identify and optimize.
"""


def find_duplicates_inefficient(items: list) -> list:
    """
    Find duplicate items in a list.
    
    Problem: Uses nested loops resulting in O(n²) time complexity.
    This is very slow for large lists.
    
    Args:
        items: List of items to check for duplicates.
    
    Returns:
        List of duplicate items.
    """
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


def count_word_frequency_inefficient(text: str) -> dict:
    """
    Count the frequency of each word in a text.
    
    Problem: Repeatedly checks if word exists in dictionary,
    then updates. Could use collections.Counter or dict.get().
    
    Args:
        text: The text to analyze.
    
    Returns:
        Dictionary mapping words to their frequencies.
    """
    words = text.lower().split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    return frequency


def filter_and_transform_inefficient(numbers: list) -> list:
    """
    Filter even numbers and square them.
    
    Problem: Uses multiple loops when a single list comprehension would suffice.
    Creates unnecessary intermediate lists.
    
    Args:
        numbers: List of numbers to process.
    
    Returns:
        List of squared even numbers.
    """
    # First filter
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    
    # Then transform
    squared = []
    for n in evens:
        squared.append(n ** 2)
    
    return squared


if __name__ == "__main__":
    # Test find_duplicates
    test_list = [1, 2, 3, 2, 4, 3, 5]
    print(f"Duplicates: {find_duplicates_inefficient(test_list)}")
    
    # Test word frequency
    test_text = "the quick brown fox jumps over the lazy dog the fox"
    print(f"Word frequency: {count_word_frequency_inefficient(test_text)}")
    
    # Test filter and transform
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Squared evens: {filter_and_transform_inefficient(test_numbers)}")
