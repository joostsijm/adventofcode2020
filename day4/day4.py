"""Day4"""

import re


REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
INT_FIELDS = ['byr', 'iyr', 'eyr']
EYE_COLOR = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] 

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
            if field in INT_FIELDS:
                value = int(value)
            if field == 'hgt':
                value = {
                    'value': int(re.findall(r'\d*', value)[0]),
                    'length': re.sub(r'\d+', '', value),
                }
            passport[field] = value
    if check_required(passport):
        valid_passports.append(passport)
    else:
        invalid_passports.append(passport)

    for passport in sorted(valid_passports, key=lambda k: k['hgt']['value']):
        print_passport(passport)
    print('Valid passports   : {}'.format(len(valid_passports)))
    print('invallid passports: {}'.format(len(invalid_passports)))


def print_passport(passport):
    """Print passport"""
    for key in sorted(passport):
        if key == 'cid':
            continue
        print('{}: {} '.format(key, passport[key]), end='')
    print()

def check_required(passport):
    """Check for all required fields in passport"""
    for field in REQUIRED:
        if field not in passport:
            return False
    if passport['byr'] < 1920 or passport['byr'] > 2002:
        return False
    if passport['iyr'] < 2010 or passport['iyr'] > 2020:
        return False
    if passport['eyr'] < 2020 or passport['eyr'] > 2030:
        return False
    if passport['hgt']['length'] == 'cm':
        if passport['hgt']['value'] < 150 or passport['hgt']['value'] > 193:
            return False
    if passport['hgt']['length'] == 'in':
        if passport['hgt']['value'] < 59 or passport['hgt']['value'] > 76:
            return False
    if not passport['hgt']['length']:
        return False
    if len(re.findall(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport['hcl'])) == 0:
        return False
    if passport['ecl'] not in EYE_COLOR:
        return False
    if len(re.findall(r'\b\d{9}\b', passport['pid'])) == 0:
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
