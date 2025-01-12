class Counter:
    counter = 0

    def __init__(self):
        Counter.counter += 1

    def get_counter(self):
        return Counter.counter

if __name__ == '__main__':
    counter = Counter()
    print(counter.get_counter())
    counter2 = Counter()
    print(counter2.get_counter())