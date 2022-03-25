def binary_search(a, x):
    l, r, pos = 0, len(a) - 1, -1

    while l <= r:
        mid = (l + r) // 2
        if x <= a[mid]:
            pos, res, r = mid, a[mid], mid - 1
        else:
            l = mid + 1

    return '第 {} 个位置找到 {}.'.format(pos + 1, x) if x == a[pos] else 'Not found.'


print('输入数组:')
arr = list(map(int, input().strip().split()))
print('输入要查找的指:')
key: int = int(input().strip())
print(binary_search(arr, key))
