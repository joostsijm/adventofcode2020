"""Day 1"""

def main():
    """Main method"""
    numbers = []
    for line in read():
        numbers.append(int(line))
    for first_number in numbers:
        for second_number in numbers:
            for third_number in numbers:
                if first_number + second_number + third_number == 2020:
                    print(first_number * second_number * third_number)


def read():
    """Read file"""
    lines = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', ''))
    return lines

if __name__ == '__main__':
    main()
