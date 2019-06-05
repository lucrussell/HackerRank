if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0:
        print('Weird')
    else:
        if n in range(2, 5+1) or n > 20:
            print('Not Weird')
        if n in range(6, 20+1):
            print('Weird')
