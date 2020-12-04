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

def read():
    """Read file"""
    lines = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', ''))
    return lines

if __name__ == '__main__':
    main()
