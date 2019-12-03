

def main():
    with open('input.txt', 'r') as data:
        for x in range(100):
            for y in range(100):
                intcodes = [int(x) for x in data.read().split(',')]
                process(x, y, intcodes)
                data.seek(0)


def process(x, y, intcodes):
    intcodes[1] = x
    intcodes[2] = y
    for i in range(0, len(intcodes)-1, 4):
        action = intcodes[i]
        first = intcodes[i + 1]
        second = intcodes[i + 2]
        position = intcodes[i + 3]
        if action == 99:
            break
        result = calculate(action, intcodes[first], intcodes[second])
        intcodes[position] = result
    if intcodes[0] == 19690720:
        print(100 * x + y)


def calculate(index, first, second):
    if index == 1:
        return first + second
    elif index == 2:
        return first * second
    else:
        print("Unknown operation:", index)


if __name__ == '__main__':
    main()
