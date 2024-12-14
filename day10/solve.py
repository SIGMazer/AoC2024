
import os 
import time
MAP = []
RESULT = 0


def handle_input():
    with open("input.txt", "r") as file:
        for line in file:
            MAP.append(line.strip())

def is_valid(x, y):
    return 0 <= x < len(MAP) and 0 <= y < len(MAP[0])


def part1():
    visited = []
    def is_hiking(x, y):
        global RESULT
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if is_valid(x, y) == False:
            return
        for direction in directions:
            if (is_valid(x+ direction[0], y+ direction[1])) and int(MAP[y + direction[1]][x + direction[0]]) - int(MAP[y][x]) == 1:
                if MAP[y + direction[1]][x + direction[0]] == "9" and (x + direction[0], y + direction[1]) not in visited:
                    visited.append((x + direction[0], y + direction[1]))
                    RESULT += 1
                else:
                    is_hiking(x + direction[0], y + direction[1])


    for y in range(len(MAP)):
        for x in range(len(MAP[y])):
            if MAP[y][x] == "0":
                is_hiking(x, y)
                visited.clear()
    print(RESULT)

def find_trails(x, y, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if MAP[y][x] == "9":
        return 1

    trail_count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and (nx, ny) not in visited:
            if int(MAP[ny][nx]) - int(MAP[y][x]) == 1:
                visited.add((nx, ny))
                trail_count += find_trails(nx, ny, visited)
                visited.remove((nx, ny))

    return trail_count

def part2():
    total_rating = 0

    for y in range(len(MAP)):
        for x in range(len(MAP[0])):
            if MAP[y][x] == "0":
                total_rating += find_trails(x, y, set([(x, y)]))

    print(total_rating)


def main():
    handle_input()
    part1()
    part2()

if __name__ == "__main__":
    main()
