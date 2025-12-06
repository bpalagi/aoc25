import sys
import requests

def part1(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/6/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    results = [int(i) for i in input[0].split()]
    operators = [i for i in input[len(input)-1].split()]

    for i in range(1,len(input)-1):
        currLine = [int(j) for j in input[i].split()]
        for k in range(len(currLine)):
            if operators[k] == '+':
                results[k] += currLine[k]
            else:
                results[k] *= currLine[k]

    return sum(results)

def part2(session_cookie):
    response = requests.get('https://adventofcode.com/2025/day/6/input', cookies={'session': session_cookie})
    input = response.text.strip().split('\n')

    ops_line = input[-1]
    op_positions = []
    problems = []

    currIndex = 0
    while currIndex < len(ops_line):
        if ops_line[currIndex] in '+*':
            op_positions.append((currIndex, ops_line[currIndex]))
            problems.append([])
        currIndex += 1

    for i in range(len(input)-1):
        curr = 0

        for j in range(len(op_positions)):
            if j != len(op_positions)-1:
                problems[j].append(input[i][curr:op_positions[j+1][0]-1])
                curr = op_positions[j+1][0]
            else:
                problems[j].append(input[i][curr:])


    ret = 0
    for problemIndex in range(len(problems)):
        columns = []
        for _ in range(len(problems[problemIndex][0])):
            columns.append('')

        for num in problems[problemIndex]:
            for digit in range(len(num)):
                columns[digit] += num[digit]

        val = int(columns[0].strip())
        for colIndex in range(1, len(columns)):
            if op_positions[problemIndex][1] == '+':
                val += int(columns[colIndex].strip())
            else:
                val *= int(columns[colIndex].strip())

        ret += val

    return ret

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python day6.py <session_cookie>")
        sys.exit(1)
    print(part2(sys.argv[1]))
