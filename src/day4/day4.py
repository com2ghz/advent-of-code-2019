

INPUT = "172851-675869"


def main():
    splitted = INPUT.split("-")
    start = int(splitted[0])
    end = int(splitted[1])

    candidates = []
    for item in range(start, end):
        item_str = str(item)
        prev_digit = 0
        has_same_digit = False
        valid = True
        for char in item_str:
            count = item_str.count(char)
            digit = int(char)
            if digit == prev_digit:
                prev_digit = prev_digit
                has_same_digit = True
                if count % 2 > 0:
                    valid = False
                    break
            elif digit > prev_digit:
                prev_digit = digit
            else:
                valid = False
        if has_same_digit and valid:
            candidates.append(item)

    print("Part 2: Possible candidates:", len(candidates))
    print(candidates)



if __name__ == '__main__':
    main()