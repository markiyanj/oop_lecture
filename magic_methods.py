class Counter:
    def __init__(self, low, high, new_item):
        self.current = low - 1
        self.high = high
        self.new_item = new_item

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.new_item
        if self.current < self.high:
            return self.current
        raise StopIteration

for c in Counter(3, 9, 2):
    print(c)
