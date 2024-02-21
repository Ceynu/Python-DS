def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half,right_half)

def merge(left,right):
    result = []
    left_idx,right_idx = 0,0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx+=1
        else:
            result.append(right[right_idx])
            right_idx+=1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result
arr = [12,11,13,5,6,7]
sorted_array = merge_sort(arr)
print("sorted array:",sorted_array) 

size = int(input("enter the size:"))
my_sort = []
for i in range(size):
    elements = int(input("Enter the elements:"))
    my_sort.append(elements)

print("Unsorted array:",my_sort)
merge_sort(my_sort)
print("Sorted array:",my_sort)


        


