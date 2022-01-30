import time
from solver import *
from simulator import *
if __name__ == "__main__":
    startTime = time.time()
    targets = all_5letter_words
    results = [simulate(ans) for ans in targets]
    endTime = time.time()
    worst = max(results)
    mean = sum(results)/len(results)
    best = min(results)
    print(
        f"best: {best}, worst: {worst}, mean: {mean}\n" +
        f"elapsed:{endTime- startTime}"
    )
