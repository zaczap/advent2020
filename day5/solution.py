#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import sys

path_to_input = sys.argv[1]

def decode(code):
    row = code[0:7]
    col = code[7:10]
    row = int(row.replace('F', '0').replace('B', '1'), 2)
    col = int(col.replace('L', '0').replace('R', '1'), 2)
    return (row, col)

def parse_seat_id(code):
    row, col = decode(code)
    return row*8 + col

seats = []
min_seat_id = 2**10
max_seat_id = 0
with open(path_to_input) as input_file:
    for line in input_file:
        seat_id = parse_seat_id(line.strip())
        seats.append(seat_id)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        if seat_id < min_seat_id:
            min_seat_id = seat_id
            
print(min_seat_id, max_seat_id)

for seat in range(min_seat_id + 1, max_seat_id):
    if seat not in seats:
        print(seat)
