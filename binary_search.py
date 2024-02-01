def binary_search_in_recursion(arr, target):
    if len(arr) < 1:
        return None
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return binary_search_in_recursion(arr[:mid], target)
        elif arr[mid] < target:
            check = binary_search_in_recursion(arr[mid+1:], target)
            if check is not None:
                return check + mid + 1
            else:
                return None

print(binary_search_in_recursion([0, 2, 4, 5, 7, 9], -1))
