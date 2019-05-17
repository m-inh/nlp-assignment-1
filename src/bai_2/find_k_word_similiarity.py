from src.load_w2v import load_w2v
from src.bai_1.cosine import cosine
from src.bai_1.dice import dice


def find_k_word_similarity(w, k, w_dict, metric_f):
    w_distance_dict = {}
    for w_target in w_dict:
        w_distance_dict[w_target] = metric_f(w_dict[w], w_dict[w_target])

    k_w = []
    prev_min = -999999999999999999999999
    for i in range(k):
        min = None
        min_w = None
        for _w in w_distance_dict:
            w_distance = w_distance_dict[_w]
            if (min is None or w_distance < min) and (w_distance > prev_min):
                min = w_distance
                min_w = _w

        k_w.append(min_w)
        prev_min = min

    return k_w


if __name__ == "__main__":
    w = "truy_cập"
    w_dict = load_w2v("../w2v/word2vec.vec")[2]
    k = 10

    print("word: ", w)
    print("k: ", k)
    print("---------------")
    print("metric: cosine")
    print("result", find_k_word_similarity(w, k, w_dict, cosine))
    print("---------------")
    print("metric: dice")
    print("result", find_k_word_similarity(w, k, w_dict, dice))
