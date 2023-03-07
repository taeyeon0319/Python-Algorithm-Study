input_location = input()
column = int(ord(input_location[0])-ord('a')+1)
row = int(input_location[1])
count = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for step in steps:
    next_row = row + step[1]
    next_column = column + step[0]
    if next_row >= 1 and next_row<=8 and next_column>=1 and next_column<=8:
        count+=1


print(count)