import time
import os
MAP = []
RESULT = 0
LOOPING_POSITIONS = set()

def simulate_guard_with_obstruction(obstruction_pos):
    direction = (-1, 0)
    def is_wall(x, y):
        if is_valid(x, y):
            if (x, y) == obstruction_pos:
                return True
            return MAP[x][y] == '#'
        return False

    def find_guard():
        for i, row in enumerate(MAP):
            for j, cell in enumerate(row):
                if cell == '^':
                    return (i, j)
        return (-1, -1)

    def change_direction(direction):
        if direction == (-1, 0):
            return (0, 1)
        if direction == (0, 1):
            return (1, 0)
        if direction == (1, 0):
            return (0, -1)
        if direction == (0, -1):
            return (-1, 0)
        return direction

    pos = find_guard()
    visited_positions = set()
    visited_positions.add((pos, direction))  # Track position and direction
    while is_valid(*pos):
        if is_wall(pos[0] + direction[0], pos[1] + direction[1]):
            direction = change_direction(direction)
        else:
            pos = (pos[0] + direction[0], pos[1] + direction[1])

        if (pos, direction) in visited_positions:
            # The guard is stuck in a loop
            return True
        visited_positions.add((pos, direction))
    return False

def part2():
    global LOOPING_POSITIONS
    for x in range(len(MAP)):
        for y in range(len(MAP[0])):
            if MAP[x][y] == '#' or MAP[x][y] == '^':  # Can't place obstruction on a wall or the guard's starting position
                continue
            if simulate_guard_with_obstruction((x, y)):
                LOOPING_POSITIONS.add((x, y))


def handle_input():
    with open('input.txt', 'r') as f:
        for line in f:
            MAP.append(line.strip())

def is_valid(x, y):
    return 0 <= x < len(MAP) and 0 <= y < len(MAP[0])

def part1():
    global RESULT
    direction = (-1, 0)
    def is_wall(x, y):
        if is_valid(x, y):
            return MAP[x][y] == '#'

    def find_guard():
        for i, row in enumerate(MAP):
            for j, cell in enumerate(row):
                if cell == '^':
                    return (i, j)
        return (-1, -1)
    def change_direction(direction):
        if direction == (-1, 0):
            return (0, 1)
        if direction == (0, 1):
            return (1, 0)
        if direction == (1, 0):
            return (0, -1)
        if direction == (0, -1):
            return (-1, 0)
        return direction

    pos = find_guard()
    map = MAP.copy()
    map[pos[0]] = map[pos[0]][:pos[1]] + 'X' + map[pos[0]][pos[1] + 1:]
    while is_valid(*pos):
        if is_wall( pos[0] + direction[0], pos[1] + direction[1]):
            direction = change_direction(direction)
            continue
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        if is_valid(pos[0], pos[1]) and map[pos[0]][pos[1]] == 'X':
            continue
        if is_valid(pos[0], pos[1]):
            map[pos[0]] = map[pos[0]][:pos[1]] + 'X' + map[pos[0]][pos[1] + 1:]
        # print('\n'.join(map))
        # print(RESULT)
        # time.sleep(0.1)
        # os.system('clear')
        RESULT += 1

def main():
    handle_input()
    part1()
    print(RESULT)
    part2()
    print(len(LOOPING_POSITIONS))

if __name__ == '__main__':
    main()
