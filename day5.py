import sys
import requests

def part1(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/5/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n\n')

    freshRanges = input[0].split('\n')
    availableIds = input[1].split('\n')

    ret = 0

    for id in availableIds:
        id_num = int(id)
        for line in freshRanges:
            l, r = line.split('-')
            if int(l) <= id_num <= int(r):
                ret += 1
                break
            
    return ret

def part2(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/5/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n\n')

    freshRanges = input[0].split('\n')

    intervals = []
    for line in freshRanges:
        l, r = line.split('-')
        intervals.append((int(l), int(r)))
    
    intervals.sort()
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
            print(merged)
    
    total = sum(end - start + 1 for start, end in merged)
    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day5.py <session_cookie>")
        sys.exit(1)
    print(part2(sys.argv[1]))
