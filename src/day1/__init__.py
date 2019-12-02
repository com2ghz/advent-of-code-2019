import math


def main():
    data = open('input.txt', "r")

    required_fuel = 0
    total_required_fuel = 0
    for line in data.readlines():
        num = int(line)
        fuel = calculate_fuel(num)
        required_fuel += fuel
        total = fuel
        while fuel > 0:
            fuel = calculate_fuel(fuel)
            fuel = fuel if fuel > 0 else 0
            total += fuel
        total_required_fuel += total

    print('Part 1:', required_fuel)
    print('Part 2:', total_required_fuel)


def calculate_fuel(num):
    return math.floor(num / 3) - 2


if __name__ == '__main__':
    main()
