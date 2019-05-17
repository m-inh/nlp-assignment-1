import math


def dot(v, w):
    rs = 0
    for i in range(len(v)):
        rs += v[i] * w[i]
    return rs


def norm2(v):
    rs = 0
    for i in range(len(v)):
        rs += v[i] * v[i]
    return math.sqrt(rs)


def cosine(v, w):
    return dot(v, w) / (norm2(v) * norm2(w))


if __name__ == "__main__":
    v = [1, 1, 3]
    w = [1, 1, 4]

    print("v: ", v)
    print("w: ", w)
    print("cosine v, w: ", cosine(v, w))
