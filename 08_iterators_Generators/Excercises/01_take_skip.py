class take_skip:  # the reason of smaller letters because it is USED AS FUNCTION
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = -1  # so we don't change count

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count - 1:
            raise StopIteration

        self.iterations += 1

        return self.iterations * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
