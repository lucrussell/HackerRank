from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    parts = input().split(' ')
    name = ' '.join(parts[:-1])
    price = int(parts[-1])
    d[name] = int(d.get(name, 0)) + price
for k, v in d.items():
    print('{} {}'.format(k, v))
