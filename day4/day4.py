"""Day4"""


REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def main():
    """Main method"""
    valid_passports = []
    invalid_passports = []
    passport = {}
    for line in read():
        if not line:
            if check_required(passport):
                valid_passports.append(passport)
            else:
                invalid_passports.append(passport)
            passport = {}
            continue
        for item in line.split(' '):
            field, value = item.split(':')
            passport[field] = value
    if check_required(passport):
        valid_passports.append(passport)
    else:
        invalid_passports.append(passport)

    print('Valid passports   : {}'.format(len(valid_passports)))
    print('invallid passports: {}'.format(len(invalid_passports)))

def check_required(passport):
    """Check for all required fields in passport"""
    for field in REQUIRED:
        if field not in passport:
            return False
    return True

def read():
    """Read file"""
    lines = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', ''))
    return lines

if __name__ == '__main__':
    main()
