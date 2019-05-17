def min(a, b):
    if a > b:
        return a
    else:
        return b


def dice(v, w):
    min_arr = []
    for i in range(len(v)):
        min_arr.append(min(v[i], w[i]))
    return (2 * sum(min_arr)) / (sum(v) + sum(w))


v = [1, 1]
w = [1, 1, 4]

print("dice v, w: ", dice(v, w))
