from itertools import product

if __name__ == '__main__':
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    l1 = list(product(a, b))
    l1.sort()
    print(' '.join(str(e) for e in l1))
