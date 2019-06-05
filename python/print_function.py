if __name__ == '__main__':
    n = int(input())
    res = []
    for i in range(1, n+1):
        res.append(i)
    print(*res, sep='')