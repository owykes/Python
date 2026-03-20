from algorithms.utils.helper import generate_list 
import random

def partition(arr, low, high):
    """
    Partition the array using Lomuto partition scheme.
    
    Args:
        arr: List of elements
        low: Starting index
        high: Ending index
    
    Returns:
        Index of the pivot after partition
    """
    # Randomised pivot for better average performance
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:  # handles duplicates better
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    """
    Sorts the array in-place using QuickSort.
    
    Time Complexity:
        Average: O(n log n)
        Worst: O(n^2)
    
    Space Complexity:
        O(log n) due to recursion
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == "__main__":
    data = generate_list()
    print(f"Orignal array: {data}")
    quick_sort(data, 0, len(data) - 1)
    print("Sorted array:", data)