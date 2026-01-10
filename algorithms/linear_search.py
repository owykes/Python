from helper import generate_list
from helper import get_target

def linear_search(arr, target):
    """Linear search for target in list, time complexity is: worst case O(n), average O(n), best case O(1) 
    you check every element in the list sequentially until you find the target"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    #Update argument to change n
    my_list = generate_list()
    target_value = get_target(my_list)
    result = linear_search(my_list, target_value)

    print(f"{my_list} and the target value is {target_value}. index of target value in the array is {result}")
