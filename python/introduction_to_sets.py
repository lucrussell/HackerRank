def average(array):
    s = set(array)
    s1 = sum(s)
    s2 = s1/len(s)
    return '{:0.3f}'.format(s2)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)