import codecs

def load_w2v(input_fname):
    with codecs.open(input_fname, encoding='utf-8') as f:
        vocab_size, embedding_dim = f.readline().split()
        vocab_size = int(vocab_size)
        embedding_dim = int(embedding_dim)

        vocab = {}
        for l in f:
            w, vec = l.split(' ', maxsplit=1)
            vocab[w] = list(map(float, vec.split()))

        return vocab_size, embedding_dim, vocab