from collections import Counter
import random

def main():
    stuff = Counter(random.randint(1,2) for _ in xrange(1000))
    for i in sorted(stuff.items()): print i

if __name__=="__main__":
    main()

