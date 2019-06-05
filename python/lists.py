def insert(res, line):
    res.insert(int(line[1]), int(line[2]))
    return res


def pr(res, line):
    print(res)
    return res


def remove(res, line):
    res.remove(int(line[1]))


def append(res, line):
    res.append(int(line[1]))


def sort(res, line):
    res.sort()


def pop(res, line):
    res.pop()


def reverse(res, line):
    res.reverse()


if __name__ == '__main__':
    N = int(input())
    contents = []
    while True:
        try:
            x = input().split()
        except EOFError:
            break
        contents.append(x)
    res = []
    for line in contents:
        cmd = line[0]
        if cmd == 'print':
            cmd = 'pr'
        eval(cmd)(res, line)
