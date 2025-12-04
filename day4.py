import sys
import requests



def part1(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/4/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    ret = 0

    for y in range(len(input)):
        for x in range(len(input[y])):

            if input[y][x] != '@':
                continue

            # sum surrounding roles
            surrouding = 0

            for j in (-1,0,1):
                if y+j < 0 or y+j >= len(input):
                    continue
                for k in (-1,0,1):
                    if x+k < 0 or x+k >= len(input[y]):
                        continue
                    if input[y+j][x+k] == '@' and not (j==0 and k==0):
                        surrouding += 1

            if surrouding < 4:
                ret += 1

    return ret

def part2(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/4/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')
    input = [list(row) for row in input]

    curr = [row[:] for row in input]

    removed = 0
    keep_going = True

    while keep_going:

        input = [row[:] for row in curr]
        keep_going = False

        for y in range(len(input)):
            for x in range(len(input[y])):

                if input[y][x] != '@':
                    continue

                # sum surrounding roles
                surrouding = 0

                for j in (-1,0,1):
                    if y+j < 0 or y+j >= len(input):
                        continue
                    for k in (-1,0,1):
                        if x+k < 0 or x+k >= len(input[y]):
                            continue
                        if input[y+j][x+k] == '@' and not (j==0 and k==0):
                            surrouding += 1

                if surrouding < 4:
                    # can be removed.
                    curr[y][x] = '.'
                    keep_going = True
                    removed+=1

    return removed


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day4.py <session_cookie>")
        sys.exit(1)
    print(part2(sys.argv[1]))
    