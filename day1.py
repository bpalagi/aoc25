import requests
import sys

def calcChange(val):
    if val[0] == 'L':
        return -int(val[1:])
    return int(val[1:])

def main(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/1/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    count = 50
    ret = 0

    for i in input:
        count+= calcChange(i)
        count %= 100
        if count == 0:
            ret += 1

    return ret

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day1.py <session_cookie>")
        sys.exit(1)
    print(main(sys.argv[1]))
