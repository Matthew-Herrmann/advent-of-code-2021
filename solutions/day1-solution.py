def main():
    lines = get_input()
    lines = list(map(lambda x: int(x), lines))

    # Part 1
    count = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            count += 1
    print(f"Part 1: {count}")

    # Part 2
    count = 0
    for i in range(3, len(lines)):
        if lines[i] > lines[i - 3]:
            count += 1
    print(f"Part 2: {count}")


def get_input():
    with open("day1-input.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
