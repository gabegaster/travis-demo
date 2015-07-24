from collections import Counter
import random

def main():
    stuff = Counter(random.randint(1,100) for _ in xrange(1000))
    return sorted(stuff.items())

if __name__=="__main__":
    main()

