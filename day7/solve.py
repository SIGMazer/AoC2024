import itertools

OPERATIONS = []
RESULT = 0

def handle_input():
    f= open("input.txt", "r").readlines()
    for line in f:
        OPERATIONS.append(line.strip())

def parse_operation(operation):
    operation = operation.split(":")
    return operation[0], operation[1].split()

def part1():
    global RESULT

    def check_result(operation):
        global RESULT
        result, operation = parse_operation(operation)
        op_lists = itertools.product(['+', '*'], repeat=len(operation) - 1)

        res = 0
        for op_list in op_lists:
            operationCopy = list(map(int,operation.copy()))
            res = operationCopy[0]
            for i in range(len(op_list)):
                if op_list[i] == '+':
                    res += operationCopy[i + 1]
                elif op_list[i] == '*':
                    res *= operationCopy[i + 1]
            if res == int(result):
                RESULT += int(result)
                return 
            res = 0

    for operation in OPERATIONS:
        check_result(operation)

def cat_numbers(num1, num2):
    num_digits = len(str(num2))
    return num1 * (10 ** num_digits) + num2



def part2():
    global RESULT
    RESULT = 0
    def check_result(operation):
        global RESULT
        result, operation = parse_operation(operation)
        op_lists = itertools.product(['+', '*','||'], repeat=len(operation) - 1)

        res = 0
        for op_list in op_lists:
            operationCopy = list(map(int,operation.copy()))
            res = operationCopy[0]
            for i in range(len(op_list)):
                if op_list[i] == '+':
                    res += operationCopy[i + 1]
                elif op_list[i] == '*':
                    res *= operationCopy[i + 1]
                elif op_list[i] == '||':
                    res = cat_numbers(res, operationCopy[i + 1])
            if res == int(result):
                RESULT += int(result)
                return 
            res = 0

    for operation in OPERATIONS:
        check_result(operation)

def main():
    handle_input()
    part1()
    print(RESULT)
    part2()
    print(RESULT)

if __name__ == "__main__":
    main()
