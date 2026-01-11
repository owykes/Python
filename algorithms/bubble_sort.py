from helper import generate_list

def bubble_sort(arr):
    """ Repeatedly compare adjacent elements potentially making multiple
    passess through the list to sort. Best case O(n), Average O(n^2), worst case O(n^2)"""
    print(arr)
    for i in range(len(arr) -1, 0 , -1):
        no_swap = True
        for j in range(0 , i):
            if arr[j + 1] < arr [j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                no_swap = False 
                # Print tracks sort
                print(arr)
        if no_swap:
            return arr    
    return arr

if __name__ == "__main__":
    # Update argument to change n
    my_list = generate_list()
    result = bubble_sort(my_list)
    print(f"sorted list {result}")


