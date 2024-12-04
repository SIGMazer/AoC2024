from collections import Counter 
IDS1 = []
IDS2 = []
RES1 = 0
RES2 = 0
C = Counter()


def handle_input():
    global C
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            a = line.split()
            if a == []:
                continue
            IDS1.append(int(a[0]))
            IDS2.append(int(a[1]))
    C = Counter(IDS2)


def part1(list1, list2):
    global RES1
    min1 = min(list1)
    min2 = min(list2)
    RES1 += abs(min1 - min2)

def part2():
    global RES2
    for i in IDS1:
        if i in C.keys():
            RES2 += i * C.get(i)



def main(): 
    handle_input()
    # for i in range(len(IDS1)):
    #     part1(IDS1, IDS2)
    #     IDS1.remove(min(IDS1))
    #     IDS2.remove(min(IDS2))
    # print(RES1)
    part2()
    print(RES2)



if __name__ == '__main__':
    main()

