def merge(list1, list2):
    combine =  []
    i = 0 
    j = 0
    while i < len(list1)  and j < len(list2):
        if list1[i] < list2[j]:
            combine.append(list1[i])
            i = i + 1
            
        else:
            combine.append(list2[j])
            j = j + 1
    while i < len(list1):
        combine.append(list1[i])
        i += 1
    while j < len(list2):
        combine.append(list2[j])
        j += 1
    return combine

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = int(len(arr)/2)
    left = merge_sort(arr[0:middle])
    right = merge_sort(arr[middle:len(arr)])
    return merge(left,right)

original_list = [8,3,5,4,7,6,2,1]
print("Original List:", original_list)
sorted_list = merge_sort(original_list)
print("Sorted List:", sorted_list)
    