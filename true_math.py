from math import inf


def divide(first, second):
    if second != 0:
        result = first / second
    else:
        result = inf
    return result

# res = divide(15,0)
# print(res)