def wrap(string, max_width):
    lst = list(string)
    res = []
    for i in range(0, len(string), max_width):
        chunk = string[i:i + max_width]
        res.append(chunk)
    return '\n'.join(res)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
