from collections import defaultdict
RULES = defaultdict(list)
ORDER = []
UNORDER = []
RESULT = 0

def parse_input():
    inn = open("input.txt", "r").read().split("\n")
    is_rules = True
    for line in inn:
        if line == "":
            is_rules = False
            continue
        if is_rules:
            key, val = line.split("|")
            if key not in RULES:
                RULES[key] = []
            RULES[key].append(val)
        else:
            ORDER.append(line.split(","))

def part1():
    global RESULT
    def check_rule(i, rules, order):
        while i < len(order):
            if order[i] in rules:
                rules.remove(order[i])
            i += 1
        if not rules:
            return True 
        return False
    def check_order(order):
        for i, page in enumerate(order):
            rules = list(filter(lambda x: x in order, RULES[page]))
            if not check_rule(i+1, rules, order):
                return False
        return True
    global RESULT
    for order in ORDER:
        if check_order(order):
            RESULT += int(order[int(len(order)/2)])
        else:
            UNORDER.append(order)

def part2():
    global RESULT
    RESULT = 0

    def check_and_order(order):
        ordered = []
        remaining = set(order)

        # Continue until all pages are ordered
        while remaining:
            for page in order:
                if page not in remaining:
                    continue

                # Check if all pages that should come before this page are already in ordered list
                can_add = True
                for rule in RULES[page]:
                    if rule in remaining:
                        can_add = False
                        break

                if can_add:
                    ordered.append(page)
                    remaining.remove(page)
                    break

        return ordered

    # Process all unordered orders
    for order in UNORDER:
        ordered = check_and_order(order)
        middle_page = ordered[len(ordered) // 2]
        RESULT += int(middle_page)

            


def main():
    parse_input()
    part1()
    print(RESULT)
    part2()
    print(RESULT)


if __name__ == "__main__":
    main()
