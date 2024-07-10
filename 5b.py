#5b) Develop a program to implement Binary search.

def binser(arr, tar):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low +high) // 2

        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = input("enter the arr")
arr = [int(x) for x in arr.split()]

tar = int(input("enter target"))

result = binser(arr, tar)

if result == -1:
    print(f"target {tar} is not in arr")
else:
    print (f"target is found at index {result}")
