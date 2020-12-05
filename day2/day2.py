"""Day 2"""

def main():
    """Main method"""
    valid_passports = 0
    for line in read():
        policy, password = line.split(': ')
        times, letter = policy.split(' ')
        first_position, second_position = times.split('-')
        first_position = int(first_position) - 1
        second_position = int(second_position) - 1
        print(first_position, second_position, letter, password)
        valid = False
        if password[first_position] == letter:
            valid = not valid
        if password[second_position] == letter:
            valid = not valid
        if valid:
            valid_passports += 1
    print(valid_passports)




def read():
    """Read file"""
    lines = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', ''))
    return lines

if __name__ == '__main__':
    main()
