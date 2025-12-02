import sys
import requests


def part1(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/2/input', cookies={'session': session_cookie})
    input = response.text.strip().split(',')

    ret = 0

    for i in input:
        vals = [int(x) for x in i.split('-')]

        for val in range(vals[0], vals[1] + 1):
            if part1containsRepeat(val):
                ret += val

    return ret

def part1containsRepeat(val):
    val = str(val)
    return val[:len(val) // 2] == val[len(val) // 2:]

def day2(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/2/input', cookies={'session': session_cookie})
    input = response.text.strip().split(',')

    ret = 0

    for i in input:
        vals = [int(x) for x in i.split('-')]

        for val in range(vals[0], vals[1] + 1):
            if part2containsRepeats(val):
                ret += val

    return ret

def part2containsRepeats(val):
    # loop of the current repeat length
    for i in range(1, len(str(val)) // 2 + 1):
        # split the string into chunks of length i, and validate they're all equal
        chunks = [str(val)[j:j + i] for j in range(0, len(str(val)), i)]
        if len(set(chunks)) == 1:
            return True
    return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day2.py <session_cookie>")
        sys.exit(1)
    print(day2(sys.argv[1]))
