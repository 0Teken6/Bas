def binary_search(lst, target):
    left = 0
    right = len(lst) 
    while left < right:
        mid = (right + left) // 2
        if lst[mid] == target:
            return mid + 1
        elif lst[mid] > target:
            right = mid
        else:
            left = mid
    return 'Not found'

ls = []
i = input('list: ')
for a in i.split(', '):
    ls.append(int(a))
tar = int(input('Target: '))
ls.sort()
print(ls)
print("Index: ", binary_search(ls, tar))
