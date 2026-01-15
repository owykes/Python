from helper import generate_list

def selection_sort(arr):
    """Sort the list in place by repeatedly selecting the smallest remaining element
    best case: O(n^2) worst case: 0(n^2)"""

    print(arr)
    n = len(arr)
    for i in range(n -1):
        #assume the current position holds the minimum element
        min_so_far = i
        # iterate through the unsorted portion, to find the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_so_far]:
                #update if smaller elemnt is found
                min_so_far = j
        #swap smallest to orrect position
        arr[i], arr[min_so_far] = arr[min_so_far], arr[i]
    
    return arr

if __name__ == "__main__":
    my_list = generate_list()
    print(selection_sort(my_list))