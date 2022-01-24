import sys
from solver import *


def simulate_reply(input_word, answer):
    reply = []
    for input_letter, ans_letter in zip(input_word, answer):
        if input_letter == ans_letter:
            reply.append(LetterReply.CORRECT)
        elif input_letter in answer:
            reply.append(LetterReply.EXISITS)
        else:
            reply.append(LetterReply.NOTIN)
    return reply


def simulate(answer):
    ans_candidates = all_5letter_words
    input_word = FIRST_ANSWER
    for turn in range(1, MAX_TURN+1):
        print(f"answer candidates: {len(ans_candidates)}")
        print(f"trun{turn} input: {input_word}")
        reply = simulate_reply(input_word, answer)
        if reply == [LetterReply.CORRECT]*5:
            print("solved")
            break
        ans_candidates = filter_by_reply(ans_candidates, input_word, reply)
        input_word = pararell_search(ans_candidates)


if __name__ == "__main__":
    simulate(sys.argv[1])
