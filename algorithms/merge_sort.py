from helper import generate_list

def merge_sort(arr):
    """ Splits the list into two halves, sorts each half recursively, 
    best case: O(nlogn) worst case: O(nlogn) """

    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    """merges the two sorted halves"""
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
    
if __name__ == "__main__":
    my_list = generate_list()
    print(my_list)
    print(merge_sort(my_list))