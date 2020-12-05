"""Day 5"""

# 0 .. 127
# 0 .. 7

#0  127
#0  63
#32 63
#32 47
#40 47
#44 47
#44 45
#44

def main():
    """Main method"""
    seat_list = {}
    max_seat_id = 0
    for boardpass in read():
        start_row = 0
        end_row = 127
        start_seat = 0
        end_seat = 7
        row = 0
        seat = 0
        for character in boardpass:
            if character == 'F':
                end_row = int(start_row + (end_row - start_row + 1) / 2 - 1)
            if character == 'B':
                start_row = int(start_row + (end_row - start_row + 1) / 2)
            if start_row == end_row:
                row = start_row
            if character == 'L':
                end_seat = int(start_seat + (end_seat - start_seat + 1) / 2 - 1)
            if character == 'R':
                start_seat = int(start_seat + (end_seat - start_seat + 1) / 2)
            if start_seat == end_seat:
                seat = start_seat
        seat_id = (row * 8 + seat)
        print('{:4n} {:2n} {:3n}'.format(row, seat, seat_id))
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        seat_list[seat_id] = True
        
    print('max: {}'.format(max_seat_id))
    for seat in range(1, max_seat_id):
        if seat not in seat_list and seat + 1 in seat_list and seat - 1 in seat_list:
            print('your seat: {}'.format(seat))


def read():
    """Read file"""
    lines = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            lines.append(line.replace('\n', ''))
    return lines

if __name__ == '__main__':
    main()
