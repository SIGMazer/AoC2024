
import re



inn = open('input.txt', 'r').read()

def parse_input(inn, pt):
    stms = []
    if pt == 1:
        stms = re.findall(r"mul\(\d+,\d+\)", inn)
    else: 
        stms = re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", inn)
    res = []
    is_do = True 
    for i, stm in enumerate(stms):
        if pt ==1:
            res.append(tuple(map(int, re.findall(r"\d+", stm))))
        if pt == 2:
            if stm == "don't()":
                is_do = False
            elif stm == "do()":
                is_do = True
            else:
                if is_do:
                    res.append(tuple(map(int, re.findall(r"\d+", stm))))


    return res


def part1(inn):
    res = 0
    for a, b in parse_input(inn, 1):
        res += a * b
    return res

def part2(inn):
    res = 0
    for a, b in parse_input(inn, 2):
        res += a * b
    return res


def main():
    print(part1(inn))
    print(part2(inn))

if __name__ == '__main__':
    main()
