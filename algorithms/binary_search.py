from helper import generate_list, get_target

def binary_search(arr, target):
    """log2(n) divide the list in half each time"""
    low = 0
    high = len(arr)-1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid, steps
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return None, steps

if __name__ == "__main__":
    my_list = generate_list()
    sorted_list = sorted(my_list)
    target_value = get_target(sorted_list) 
    result = binary_search(sorted_list, target_value)
    
    print(f"{sorted_list}  with the target of {target_value} and the result is {result}")