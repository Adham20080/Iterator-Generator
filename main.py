import timeit

ii = [3, 4, 5, "Hello World"]
i = iter(ii)


try:
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
except StopIteration:
    print("No more")

for a in i:
    try:
        print(a)
    except StopIteration:
        print("Stopped")

class PowTwo:
    def __init__(self, limit=0):
        self.limit = limit

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.limit:
            pow_number = 2 ** self.n
            self.n += 1
            return pow_number
        else:
            raise StopIteration


number = PowTwo(5)
iterator = iter(number)

try:
    while True:
        print(next(iterator))
except StopIteration:
    print("StopIteration")

for i in iterator:
    try:
        print(i)
    except StopIteration:
        print("StopIteration")


def generators():
    for x in range(10_000):
        yield x


def generator_return():
    temp = []
    for i in generators():
        if i == 1_000:
            break
    return temp


def for_loop():
    temp_list: list[int] = []
    for x in range(10_000):
        temp_list.append(x)

    return temp_list


if __name__ == '__main__':
    time_for = timeit.timeit(stmt=for_loop, number=10_000)
    time_yield = timeit.timeit(stmt=generators, number=10_000)

    print("For loop", round(time_for, 5))
    print("Yield   ", round(time_yield, 5))
    faster = (time_for / time_yield) * 100
    print(f"{(round(faster, 2))} % tez")
