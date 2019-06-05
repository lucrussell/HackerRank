if __name__ == '__main__':
    list_to_sort = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l = [name, score]
        list_to_sort.append(l)
    list_to_sort.sort(key=lambda x: int(x[1]))

    d = {}
    for item in list_to_sort:
        name = item[0]
        score = item[1]
        if d.get(score):
            d[score].append(name)
        else:
            d[score] = [name]
    unique_scores = list(d.keys())
    unique_scores.sort()
    me = unique_scores[1]

    second_lowest = d.get(me)
    second_lowest.sort()
    for item in second_lowest:
        print(item)