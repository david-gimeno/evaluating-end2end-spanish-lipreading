import argparse
import numpy as np
import pandas as pd
from unidecode import unidecode

def read_csv(dataset_path):
    return pd.read_csv(dataset_path)

def get_lm_vocabulary(lm):
    lm_vocab = {}
    transcriptions = lm["transcriptions"].tolist()
    for sentence in transcriptions:
        for word in sentence.split():
            if lm_vocab.get(word) is None:
                lm_vocab[word] = 1
            else:
                lm_vocab[word] += 1

    return lm_vocab

def get_top_vocabulary(dataset, top):
    return dataset["database_word"].tolist()[:top]

def get_vocabulary(dataset):
    return dataset["database_word"].tolist()

def get_frequency(dataset):
    return dataset["database_freq"].tolist()

def get_running_words(vocabulary, frequency):
    running_words = []
    for vocab, freq in zip(vocabulary, frequency):
        for f in range(freq):
            running_words.append(vocab)

    assert len(running_words) == np.array(frequency).sum()
    return running_words

def vocabulary_intersection(vocabulary_a, vocabulary_b):
    return list(set(vocabulary_a).intersection(set(vocabulary_b)))

def running_words_intersection(running_words, vocabulary):
    return [r for r in running_words if r in vocabulary]

def compute_percentage(reference_set, intersection_set):
    return round(len(intersection_set) * 100 / len(reference_set), 2)


if __name__ == "__main__":
    # -- parsing command line arguments
    parser = argparse.ArgumentParser(description="Computing Zipf's law statistics.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("--train-path", default="./zipf_stats/VLRF/train.csv", type=str, help="Path where the train's Zipf's law statistics are.")
    parser.add_argument("--test-path", default="./zipf_stats/VLRF/test.csv", type=str, help="Path where the test's Zipf's law statistics are.")
    parser.add_argument("--lm-path", default="./SpanishLM/commonvoice_librispeech_tedx_vlrf.csv", type=str, help="Path where the text for estimating the LM is.")
    parser.add_argument("--top-nwords", default=500, type=int, help="N highest-frequency words.")
    args = parser.parse_args()

    # -- reading text used to estimate the LM
    lm = read_csv(args.lm_path)

    # -- computing vocabulary of that LM's text
    lm_v = get_lm_vocabulary(lm)

    # -- reading statistics
    train = read_csv(args.train_path)
    test = read_csv(args.test_path)

    # -- vocabulary of each dataset & test running words
    train_v = get_vocabulary(train)
    test_v = get_vocabulary(test)

    print(f"\n\033[1mtrain-v:\033[0m {len(train_v)} words")
    print(f"\033[1mtest-v:\033[0m {len(test_v)} words")

    # -- test running words
    test_f = get_frequency(test)
    test_rw = get_running_words(test_v, test_f)

    print(f"\033[1mtest-rw:\033[0m {len(test_rw)} words")
    print("-"*20)

    # -- intersections
    top_v = get_top_vocabulary(train, args.top_nwords)

    test_n_train = vocabulary_intersection(test_v, train_v)
    test_n_top = vocabulary_intersection(test_v, top_v)
    testrw_n_train = running_words_intersection(test_rw, train_v)
    testrw_n_top = running_words_intersection(test_rw, top_v)

    print(f"\033[1mtest-v ∩ train-v:\033[0m {len(test_n_train)} words ({compute_percentage(test_v, test_n_train)}%)")
    print(f"\033[1mtest-v ∩ top-v:\033[0m {len(test_n_top)} words ({compute_percentage(test_v, test_n_top)}%)")
    print(f"\033[1mtest-rw ∩ train-v:\033[0m {len(testrw_n_train)} words ({compute_percentage(test_rw, testrw_n_train)}%)")
    print(f"\033[1mtest-rw ∩ top-v:\033[0m {len(testrw_n_top)} words ({compute_percentage(test_rw, testrw_n_top)}%)\n")
    print("-"*20)

    test_n_lm = vocabulary_intersection(test_v, lm_v)
    testrw_n_lm = running_words_intersection(test_rw, lm_v)

    print(f"\033[1mtest-v ∩ lm-v:\033[0m {len(test_n_lm)} words ({compute_percentage(test_v, test_n_lm)}%)")
    print(f"\033[1mtest-rw ∩ lm-v:\033[0m {len(testrw_n_lm)} words ({compute_percentage(test_rw, testrw_n_lm)}%)\n")
