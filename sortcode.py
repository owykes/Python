unsorted_list = [2,7,4,9,5,6,1,8,3]

i = int((len(unsorted_list) / 2))
pivot_number = unsorted_list[i]
lh_sort = []
rh_sort = []

for num in unsorted_list:
        
    if num < pivot_number and != i:
        lh_sort.append(num)
    else:
        rh_sort.append(num)

print(f"{lh_sort}{rh_sort}")