"""Day3"""


def main():
    """Main method"""
    slope = {}
    height = 0
    for row in read():
        slope[height] = {}
        width = 0
        for place in row:
            slope[height][width] = place
            width += 1
        height += 1

    trees = [
        calculate_trees(slope, 1, 1),
        calculate_trees(slope, 1, 3),
        calculate_trees(slope, 1, 5),
        calculate_trees(slope, 1, 7),
        calculate_trees(slope, 2, 1),
    ]
    multiplied_trees = 1
    for tree in trees:
        multiplied_trees *= tree
    print(multiplied_trees)

def calculate_trees(slope, down, right):
    """Calculate number of trees"""
    trees = 0
    for row in range(0, len(slope), down):
        position = get_position(slope, row, row * right / down)
        if position == '#':
            trees += 1
    return trees

def get_position(slope, height, width):
    """Get position from slope"""
    return slope[height][width % len(slope[0])]

def read():
    """Read file"""
    lines = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', ''))
    return lines

if __name__ == '__main__':
    main()
