#5a. Develop a program to implement Merge sort.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    ans = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            ans.append(left_arr[i])
            i += 1
        else:
            ans.append(right_arr[j])
            j += 1

    ans += left_arr[i:]
    ans += right_arr[j:]
    return ans


arr = input("enter the arr : ")
arr = [int(x) for x in arr.split()]

sorted_arr = merge_sort(arr)
print(sorted_arr)
