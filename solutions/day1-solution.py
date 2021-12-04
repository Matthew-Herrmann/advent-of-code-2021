def get_lines(path, file):
    """Return a list of lines in a given file from a given path"""
    with open(path + file) as f:
        return f.read().splitlines()


def amount_gt_previous(nums, offset):
    """Return amount of times that each number in a given list is greater than the previous at a given offset"""
    amount = 0
    for i in range(offset, len(nums)):
        if nums[i] > nums[i - offset]:
            amount += 1
    return amount


def part1(lines):
    return amount_gt_previous(lines, 1)


def part2(lines):
    return amount_gt_previous(lines, 3)


def main():
    # Input
    lines = get_lines("../resources/inputs/", "day1-input.txt")
    lines = [int(x) for x in lines]

    # Part 1
    print(f"Part 1: {part1(lines)}")

    # Part 2
    print(f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    main()
