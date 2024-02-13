it = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


class RetGen:
    def __init__(self, iterator):
        self.ite = iterator

    def __next__(self):
        d = []
        for a in self.ite:
            d.append(a ** 2)
        return f"Dooble: {d}"


obj = RetGen(it)
print(next(obj))

i = [1, 3, 5, 7, 9, 11, 13, 15]


def generator(iterator):
    yield iterator


print(*next(generator(i)))
