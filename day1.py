import requests
import sys

def calcChange(val):
    if val[0] == 'L':
        return -int(val[1:])
    return int(val[1:])

def landOnZero(session_cookie):
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


def passZero(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/1/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    count = 50
    ret = 0

    for i in input:
        change = calcChange(i)
        new_count = (count + change) % 100
        
        ret += abs(change) // 100
        
        # Partial wrap (crossed 0 once, but didn't land on it)
        if change < 0 and new_count > count and count != 0:
            ret += 1
        elif change > 0 and new_count < count and new_count != 0:
            ret += 1
        
        # Landed exactly on 0
        if new_count == 0:
            ret += 1
        
        count = new_count
        
    return ret


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day1.py <session_cookie>")
        sys.exit(1)
    print(passZero(sys.argv[1]))
