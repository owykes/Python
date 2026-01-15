from helper import generate_list

def bubble_sort(arr):
    """ Repeatedly compare adjacent elements potentially making multiple
    passess through the list to sort. Best case O(n), worst case O(n^2)"""
    print(arr)
    for i in range(len(arr) -1, 0 , -1):
        sorted = True
        for j in range(0 , i):
            if arr[j + 1] < arr [j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                sorted = False 
                # Print tracks sort
                print(arr)
        if sorted:
            return arr    
    return arr

if __name__ == "__main__":
    # Update argument to change n
    my_list = generate_list()
    result = bubble_sort(my_list)
    print(f"sorted list {result}")


