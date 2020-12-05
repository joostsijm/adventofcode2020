"""Day 2"""

def main():
    """Main method"""
    valid_passports = 0
    for line in read():
        policy, password = line.split(': ')
        times, letter = policy.split(' ')
        min_times, max_times = times.split('-')
        min_times = int(min_times)
        max_times = int(max_times)
        print(min_times, max_times, letter, password)
        character_count = 0
        for character in password:
            if character == letter:
                character_count += 1
        if min_times <= character_count <= max_times:
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
