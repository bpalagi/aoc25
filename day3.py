import sys
import requests



def part1(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/3/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    ret = 0

    for i in input:
        # identify index of max value within index 0 to len-1
        max_index = i.index(max(i[:len(i) - 1]))
        second_max_index = i.index(max(i[max_index + 1:]))
        ret += (int(i[max_index] + i[second_max_index]))

    return ret

def part2(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/3/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    ret = 0

    for i in input:
        # Greedily select 12 digits to form the largest number (preserving relative order)
        result = []
        start = 0
        for remaining in range(12, 0, -1):
            # Find the max digit in the valid range (must leave enough digits for remaining picks)
            end = len(i) - remaining + 1
            max_idx = start
            for j in range(start, end):
                if i[j] > i[max_idx]:
                    max_idx = j
            result.append(i[max_idx])
            start = max_idx + 1
        ret += int(''.join(result))

    return ret


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day3.py <session_cookie>")
        sys.exit(1)
    print(part2(sys.argv[1]))
    