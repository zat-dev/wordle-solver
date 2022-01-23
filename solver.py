import argparse
from enum import IntEnum, auto
import itertools
from multiprocessing import Pool
from sys import stderr

LETTER_NUM = 5
MAX_TURN = 6
PARARELL = 10


def get_all_5letter_words():
    words_file = "./5letter_words.txt"
    all_5letter_words = []
    with open(words_file) as file:
        for line in file:
            all_5letter_words.append(line.rstrip())
    return all_5letter_words


all_5letter_words = get_all_5letter_words()


class LetterReply(IntEnum):
    NOTIN = 1  # GRAY
    EXISITS = 2  # YELLOW
    CORRECT = 3  # GREEN


all_reply_patterns = list(itertools.product(
    [
        LetterReply.NOTIN,
        LetterReply.EXISITS,
        LetterReply.CORRECT
    ], repeat=LETTER_NUM))


def filter_by_reply(candidates, input_word, reply):
    for index, (letter, letter_result) in enumerate(zip(input_word, reply)):
        if letter_result == LetterReply.NOTIN:
            candidates = list(filter(lambda s: letter not in s, candidates))
        elif letter_result == LetterReply.EXISITS:
            candidates = list(
                filter(lambda s: letter in s and s[index] != letter, candidates))
        else:
            candidates = list(filter(lambda s: letter == s[index], candidates))
    return candidates


def search_best_input(args):
    ans_candidates, search_domain = args
    best = ((float("INF"), float("INF")), None)
    if len(ans_candidates) == 0:
        return best
    if len(ans_candidates) <= 2:
        return ((0, 0), ans_candidates[0])

    for word in search_domain:
        worst_rest_size = 0
        rest_sizes = []

        for result in all_reply_patterns:
            rest = filter_by_reply(ans_candidates, word, result)
            if len(rest) == 0:
                continue  # this reply pattern is conflict
            if len(rest) == len(ans_candidates):
                continue  # no benefit to choose this word
            worst_rest_size = max(worst_rest_size, len(rest))
            rest_sizes.append(len(rest))
        if len(rest_sizes) == 0:
            continue
        score = (worst_rest_size, sum(rest_sizes)/len(rest_sizes))
        if score < best[0]:
            best = (score, word)
    return best


def pararell_search(ans_candidates):
    p = Pool(PARARELL)
    search_size = len(all_5letter_words)//(PARARELL - 1)
    search_domains = [
        all_5letter_words[i*search_size:(i+1)*search_size]
        for i in range(PARARELL)
    ]
    args = list(map(lambda x: (ans_candidates, x), search_domains))
    results = p.map(search_best_input, args)
    return min(results, key=lambda x: x[0])[1]


def solve():
    ans_candidates = all_5letter_words
    input_word = "SERAI"  # pre calculated
    for turn in range(1, MAX_TURN+1):
        print(f"[turn{turn}] input '{input_word}' to Wordle and enter the reply")
        reply = list(map(lambda x: LetterReply(int(x)), list(input())))
        if reply == [LetterReply.CORRECT]*5:
            print("solved")
            break
        print("start calculation. wait a minute...")
        ans_candidates = filter_by_reply(ans_candidates, input_word, reply)
        input_word = pararell_search(ans_candidates)


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="""
    Wordle Solver

    input words to Wordle following this solver
    and input reply of Wordle to this terminal.

    the input reply format is:
       GRAY=1, YELLOW=2, GREEN=3
    
    for example, if Wordle reply is all gray, enter the following
       11111
    """)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    solve()
