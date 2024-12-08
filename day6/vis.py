import time
from raylib import *

MAP = []
RESULT = 0
CELL_SIZE = 5  

def handle_input():
    with open('input.txt', 'r') as f:
        for line in f:
            MAP.append(line.strip())

def is_valid(x, y):
    return 0 <= x < len(MAP) and 0 <= y < len(MAP[0])

def draw_map(map_data):
    for i, row in enumerate(map_data):
        for j, cell in enumerate(row):
            if cell == '#':  # Wall
                DrawRectangle(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE, GRAY)
            elif cell == '^':  # Guard's initial position
                DrawRectangle(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE, BLUE)
            elif cell == 'X':  # Path covered by the guard
                DrawRectangle(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE, GREEN)

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
    map_copy = [list(row) for row in MAP]
    map_copy[pos[0]][pos[1]] = 'X'
    frame = 0
    
    while is_valid(*pos):
        BeginDrawing()
        ClearBackground(RAYWHITE)
        draw_map(map_copy)
        EndDrawing()

        if is_wall(pos[0] + direction[0], pos[1] + direction[1]):
            direction = change_direction(direction)
            continue

        pos = (pos[0] + direction[0], pos[1] + direction[1])
        frame += 1

        if is_valid(pos[0], pos[1]) and map_copy[pos[0]][pos[1]] == 'X':
            continue
        if is_valid(pos[0], pos[1]):
            map_copy[pos[0]][pos[1]] = 'X'

        RESULT += 1


def main():
    global MAP

    # Initialize the map and Raylib
    handle_input()
    screen_width_scaled = len(MAP[0]) * CELL_SIZE
    screen_height_scaled = len(MAP) * CELL_SIZE
    lit: bytes = b'Map'
    InitWindow(screen_width_scaled, screen_height_scaled, lit)

    SetTargetFPS(120)

    part1()

    print(f"Result: {RESULT}")
    while not WindowShouldClose():
        BeginDrawing()
        ClearBackground(RAYWHITE)
        draw_map(MAP)
        EndDrawing()

    CloseWindow()

if __name__ == '__main__':
    main()

