def array_left_rotation(a, n, k):
    res = a[k:]
    res.extend(a[:k])
    return res


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')