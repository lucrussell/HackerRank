lines = []
for _ in range(int(input())):
    a, b = input().split()
    lines.append((a,b))

for k in lines:
    try:
        r = int(k[0])/int(k[1])
        print(int(r))
    except ZeroDivisionError as e:
        print('Error Code: integer division or modulo by zero')
    except ValueError as e:
        print('Error Code:', e)
