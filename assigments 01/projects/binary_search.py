def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left <= right:
        mid=(left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid]  < target:
            left =right +1
        else:
            right=mid-1
    return -1
arr=[1,2,7,6,10]
target=7
result=binary_search(arr,target)
if result != 1:
    print(f"Element found at index {result}")
else:
    print("Element not found")