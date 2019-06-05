if __name__ == '__main__':
    s = input()
    retVals = {
        0: False,
        1: False,
        2: False,
        3: False,
        4: False
    }
    for i in s:
        if i.isalnum():
            retVals[0] = True
        if i.isalpha():
            retVals[1] = True
        if i.isdigit():
            retVals[2] = True
        if i.islower():
            retVals[3] = True
        if i.isupper():
            retVals[4] = True

    for k, v in retVals.items():
        print(v)
