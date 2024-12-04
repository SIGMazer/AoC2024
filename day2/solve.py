
REPORTS = open('input.txt', 'r').read().split('\n')
SAFE1 = 0
SAFE2 = 0



def is_safee(report):
        if report[0] < report[1]: # increasing sequence
            return all(1 <= report[i]-report[i-1] <= 3 for i in range(1, len(report)))
        else: # decreasing sequence
            return all(1 <= report[i-1] - report[i] <= 3 for i in range(1, len(report)))



def solve():
    global SAFE1
    global SAFE2
    for i in REPORTS:
        report = i.split()
        if report == []:
            REPORTS.remove(i)
            continue
        is_safe = is_safee([int(x) for x in report])
        if is_safe is True:
            SAFE1 += 1
            SAFE2 += 1
        else: # part 2
            for i, level in enumerate(report):
                cpy = [int(x) for x in report]
                cpy.pop(i)
                is_safe = is_safee(cpy)
                if is_safe is True:
                    SAFE2 += 1
                    break





def main():
    solve()
    print(SAFE1)
    print(SAFE2)


if __name__ == '__main__':
    main()
