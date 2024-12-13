from collections import defaultdict

DISK = ''
RESULT = 0


class Block:
    def __init__(self, start, size, is_file):
        self.start: int = start
        self.size: int = size
        self.is_file = is_file
    

MAP = defaultdict(lambda: Block(0, 0, False))


def handel_input():
    global DISK
    f = open('input.txt', 'r').read().strip()
    DISK = f


def fragmenter(disk):
    map = []
    is_file = True 
    for i, item in enumerate(disk):
        start = len(map)
        for _ in range(int(item)):
            if is_file:
                map.append(i //2)
                MAP[i] = Block(start, int(item), True)
            else:
                map.append('.')
                MAP[i] = Block(start, int(item), False)
        is_file = not is_file
    return map

def swap(map, a, b):
    map[a], map[b] = map[b], map[a]
    return map

def part1():
    global RESULT
    map = fragmenter(DISK)
    i = 0
    j = len(map) - 1
    while i < j:
        while i < len(map) and map[i] != '.':
            i += 1
        while j >= 0 and map[j] == '.':
            j -= 1
        if i < j:
            map = swap(map, i, j)
            i += 1
            j -= 1

    for i, item in enumerate(map):
        if item == '.':
            break
        RESULT += i * item
        
def get_space(size, start):
    for key, item in MAP.items(): 
        if item.is_file == False and int(item.size) >= size and item.start < start:
            if int(item.size) > size:
                MAP[key] = Block(item.start + size, item.size - size, False)
            else:
                MAP[key] = Block(item.start, item.size, True)
            return item.start
    return -1

def block_swap(map, start, size, target):
    for i in range(int(size)):
        map[start + i], map[target + i] = map[target + i], map[start + i]
    return map



def part2():
    global RESULT
    RESULT = 0
    map = fragmenter(DISK)

    free_spaces = []
    for block in MAP.values():
        if not block.is_file:
            free_spaces.append((block.start, block.size))
    free_spaces.sort()  

    file_ids = sorted([key for key, block in MAP.items() if block.is_file], reverse=True)

    for file_id in file_ids:
        file_block = MAP[file_id]
        if file_block.size == 0:
            continue
        
        for i, (start, size) in enumerate(free_spaces):
            if size >= file_block.size and start < file_block.start:
                target_start = start
                map[target_start:target_start + file_block.size] = map[file_block.start:file_block.start + file_block.size]
                map[file_block.start:file_block.start + file_block.size] = ['.'] * file_block.size

                new_free_space = (target_start + file_block.size, size - file_block.size)
                if new_free_space[1] > 0:
                    free_spaces[i] = new_free_space
                else:
                    free_spaces.pop(i)

                free_spaces.append((file_block.start, file_block.size))
                free_spaces.sort()  
                break

    # Calculate checksum
    for i, item in enumerate(map):
        if item == '.':
            continue
        RESULT += i * item



def main():
    handel_input()
    part1()
    print(RESULT)
    part2()
    print(RESULT)


if __name__ == '__main__':
    main()
