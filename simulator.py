from collections import defaultdict, Counter
import enum
import sys
from solver import *


def simulate_reply(input_word, answer):
    reply = [LetterReply.NOTIN]*LETTER_NUM
    letter_count = defaultdict(int, Counter(answer))
    # porc Green
    for index, (input_letter, ans_letter) in enumerate(zip(input_word, answer)):
        if input_letter == ans_letter:
            reply[index] = LetterReply.CORRECT
            letter_count[input_letter] -= 1
    # porc Yellow
    for index, (input_letter, ans_letter) in enumerate(zip(input_word, answer)):
        if input_letter != ans_letter and letter_count[input_letter] > 0:
            reply[index] = LetterReply.EXISITS
            letter_count[input_letter] -= 1
    return reply


def simulate(answer):
    ans_candidates = all_5letter_words
    input_word = FIRST_ANSWER
    print(f"------- start simulation for {answer} --------")
    for turn in range(1, MAX_TURN+1):
        print(f"  answer candidates: {len(ans_candidates)}")
        print(f"  turn{turn} input: {input_word}")
        reply = simulate_reply(input_word, answer)
        print(f" reply: {[r.value for r in reply]}")
        if reply == [LetterReply.CORRECT]*5:
            print(" solved")
            return turn
        ans_candidates = filter_by_reply(ans_candidates, input_word, reply)
        input_word = pararell_search(ans_candidates)
    print(" failed")
    return 7


def simulate_manual(answer):
    for turn in range(1, MAX_TURN+1):
        input_word = input()
        reply = simulate_reply(input_word, answer)
        print(f" reply: {[r.value for r in reply]}")
        if reply == [LetterReply.CORRECT]*5:
            print(" solved")
            return turn
    print(" failed")
    return 7


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description="""Wordle Solver Simulator""")
    parser.add_argument("-m", "--manual", action='store_true',
                        help="simulate by manual")
    parser.add_argument("answer", help='answer of simulation')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.manual:
        simulate_manual(args.answer)
    else:
        simulate(args.answer)
