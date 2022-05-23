def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


a = [1, 4, 6, 12, 5, 66]
print(sum(a))
print(count(a))
