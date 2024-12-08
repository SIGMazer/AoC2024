
from typing import List

GRID: list[str] = []
COUNT1 = 0
COUNT2 = 0

def file_read():
    global GRID
    with open('smol.txt', 'r') as f:
        for line in f:
            GRID.append(line.strip())



def part1(word="XMAS"):
    global COUNT1
    rows = len(GRID)
    cols = len(GRID[0])

    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def search_from(y,x, dy, dx, index):
        global COUNT1
        if index == len(word):
            COUNT1 += 1
            return
        if not is_valid(y,x) or GRID[y][x] != word[index]:
            return
        search_from(y+dy, x+dx, dy, dx, index+1)

    directions = [(0,1), (1,0), (1,1), (1,-1), (-1,1), (-1,-1), (0,-1), (-1,0)]
    for i in range(rows):
        for j in range(cols):
            for dy, dx in directions:
                search_from(i, j, dy, dx, 0)




def part2():
    global COUNT2
    rows = len(GRID)
    cols = len(GRID[0])

    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def is_mas(y, x, type):
        if type == 1:
            return (is_valid(y-1, x-1) and GRID[y-1][x-1] == 'M' and 
                    is_valid(y+1, x+1) and GRID[y+1][x+1] == 'S'
                    ) or (
                    is_valid(y-1, x-1) and GRID[y-1][x-1] == 'S' and
                    is_valid(y+1, x+1) and GRID[y+1][x+1] == 'M'
                            )
        else:
            return (is_valid(y-1, x+1) and GRID[y-1][x+1] == 'M' and 
                    is_valid(y+1, x-1) and GRID[y+1][x-1] == 'S'
                    ) or (
                    is_valid(y-1, x+1) and GRID[y-1][x+1] == 'S' and
                    is_valid(y+1, x-1) and GRID[y+1][x-1] == 'M'
                            )


    def check_x_mas(y, x):
        global COUNT2

        print("A found at", y, x)
        if is_mas(y, x, 1) and is_mas(y, x, 2):
            COUNT2 += 1


    for i in range(rows):
        for j in range(cols):
            if GRID[i][j] == 'A':
                check_x_mas(i, j)





def main():
    file_read()
    part1()
    print(GRID)
    part2()
    print(COUNT1)
    print(COUNT2)


if __name__ == '__main__':
    main()

