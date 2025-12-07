import sys
import requests
from functools import lru_cache


def part1(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/7/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    prevBeams = set()
    currBeams = set()

    ret = 0

    for row in input:
        for index, char in enumerate(row):
            if char == 'S':
                currBeams.add(index)
            
            if index in prevBeams:
                currBeams.add(index)

            if char == '^' and index in prevBeams:
                currBeams.add(index+1)
                currBeams.add(index-1)
                currBeams.remove(index)
                ret += 1
            
                
        prevBeams = currBeams
        currBeams = set()

    return ret





def part2(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/7/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    # no longed need a set, beam at single index
    beam = input[0].index('S')

    @lru_cache(maxsize=None)
    def rightOrLeft(beam, currRow):
        if currRow == len(input):
            return 1
        if input[currRow][beam] == '^':
            return rightOrLeft(beam+1, currRow+1) + rightOrLeft(beam-1, currRow+1)
        return rightOrLeft(beam, currRow+1)

    return rightOrLeft(beam, 1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day7.py <session_cookie>")
        sys.exit(1)
    print(part2(sys.argv[1]))
