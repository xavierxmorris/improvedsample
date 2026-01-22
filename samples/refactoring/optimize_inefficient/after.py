"""
After: Optimized Python code with improved performance.

This module demonstrates the refactored versions with better
time complexity and more Pythonic patterns.
"""

from collections import Counter


def find_duplicates(items: list) -> list:
    """
    Find duplicate items in a list.
    
    Optimization: Uses Counter for O(n) time complexity instead of O(n²).
    
    Args:
        items: List of items to check for duplicates.
    
    Returns:
        List of duplicate items.
    """
    counts = Counter(items)
    return [item for item, count in counts.items() if count > 1]


def count_word_frequency(text: str) -> dict:
    """
    Count the frequency of each word in a text.
    
    Optimization: Uses Counter which is optimized for this exact use case.
    
    Args:
        text: The text to analyze.
    
    Returns:
        Dictionary mapping words to their frequencies.
    """
    return dict(Counter(text.lower().split()))


def filter_and_transform(numbers: list) -> list:
    """
    Filter even numbers and square them.
    
    Optimization: Single list comprehension combines filter and map operations.
    
    Args:
        numbers: List of numbers to process.
    
    Returns:
        List of squared even numbers.
    """
    return [n ** 2 for n in numbers if n % 2 == 0]


if __name__ == "__main__":
    # Test find_duplicates
    test_list = [1, 2, 3, 2, 4, 3, 5]
    print(f"Duplicates: {find_duplicates(test_list)}")
    
    # Test word frequency
    test_text = "the quick brown fox jumps over the lazy dog the fox"
    print(f"Word frequency: {count_word_frequency(test_text)}")
    
    # Test filter and transform
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Squared evens: {filter_and_transform(test_numbers)}")
