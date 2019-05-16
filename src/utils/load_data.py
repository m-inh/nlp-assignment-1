import numpy as np
import pandas as pd

from src.utils.load_w2v import load_w2v

w2v_path = "../w2v/word2vec.vec"
vicon_noun_path = "../datasets/ViCon-400/400_noun_pairs.txt"
vicon_verb_path = "../datasets/ViCon-400/400_verb_pairs.txt"
vicon_adj_path = "../datasets/ViCon-400/600_adj_pairs.txt"
vicon_all_path = "../datasets/ViCon-400/all.csv"

w2v = load_w2v(w2v_path)
w2v_dict = w2v[2]

vicon_all = pd.read_csv(vicon_all_path)

def load_data():
    _X = []
    _y = []
    miss_word = 0
    for i in range(1400):
        w1_col = vicon_all.w1.values
        w2_col = vicon_all.w2.values
        r_col = vicon_all.r.values

        try:
            w1_2_vec = w2v_dict[w1_col[i]]
            w2_2_vec = w2v_dict[w2_col[i]]
            r = r_col[i]

            x = w1_2_vec + w2_2_vec
            _X.append(x)

            if (r == "ANT"):
                _y.append(0)
            else:
                _y.append(1)
        except:
            miss_word += 1
            print("%s not found in dictionary" % w1_col[i])

    X = np.array(_X)
    y = np.array(_y)

    return X, y