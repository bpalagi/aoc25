import sys
import requests


def day2(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/2/input', cookies={'session': session_cookie})
    input = response.text.strip().split(',')

    ret = 0

    for i in input:
        vals = [int(x) for x in i.split('-')]

        for val in range(vals[0], vals[1] + 1):
            if containsRepeat(val):
                ret += val

    return ret

def containsRepeat(val):
    val = str(val)
    return val[:len(val) // 2] == val[len(val) // 2:]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day2.py <session_cookie>")
        sys.exit(1)
    print(day2(sys.argv[1]))
