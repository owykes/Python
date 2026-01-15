from helper import generate_list

def insertion_sort(arr):
    """Insertion sort takes a on item fom a list and decalres it as sorted,
    adding unsorted elements their sutiatable polace for each iteration after
    best case: O(n), worst case: O(n^2)"""
    print(arr)
    
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left hand size unotl an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        # place key at after the element just smaller than it
        arr[j + 1] = key
    
    return arr

if __name__ == "__main__":
    # update argument to change n
    my_list = generate_list()
    print(insertion_sort(my_list))
