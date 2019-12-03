

def main():
    with open('input.txt', 'r') as data:
        intcodes = [int(x) for x in data.read().split(',')]
        intcodes[1] = 12
        intcodes[2] = 2

        for index, intcode in enumerate(intcodes):
            if index == 0 or index % 4 == 0:
                action = intcodes[index]
                first = intcodes[index + 1]
                second = intcodes[index + 2]
                position = intcodes[index + 3]
                if action == 99:
                    break
                result = calculate(action, intcodes[first], intcodes[second])
                intcodes[position] = result

        print(intcodes[0])


def calculate(index, first, second):
    if index == 1:
        return first + second
    elif index == 2:
        return first * second
    else:
        print("Unknown operation:", index)


if __name__ == '__main__':
    main()
