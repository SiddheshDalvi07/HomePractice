def binary(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0 


    while low <= high:

        mid = (high+low) //2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1
        
        else:
            return mid
        
    return -1

arr = [1,23,34,45,66]
x = 1


if binary(arr,x) != -1:
    print("Element is present at index",binary(arr,x))
else:
    print("Element is not present in array")


