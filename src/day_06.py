from pathlib import Path

INPUT_PATH = Path("../inputs/day_06.txt")

with open(INPUT_PATH) as file:
    input_matrix = [ line.split() for line in file    ]

operations = input_matrix[-1]
LIST_NUMBERS = 4 # There are always 4 numbers being operated on
#Part I
# count = 0
# digits= []
# for i in range(0, len(operations)):
#     operation = operations[i]
#     digits= [row[i] for row in input_matrix if row!=operations]
#
#     if operation =="*":
#         output = 1
#         for digit in digits:
#             output*=int(digit)
#     else:
#         output= 0
#         for digit in digits:
#             output+=int(digit)
#     count+= output

#PART II
calculations=len(operations)
lengths = [ ]
for i in range(0,calculations):
    max_length = max(len(input_matrix[0][i]),
                     len(input_matrix[1][i]),
                     len(input_matrix[2][i]),
                     len(input_matrix[3][i]))
    lengths.append(max_length)

count = 0
all_numbers = [[[]for i in range(0,calculations)] for j in range(0,5) ]
line_number = 0
pointer = 0
#Extract and Transform
with open(INPUT_PATH) as file:
    for line in file:
        pointer= 0
        for i in range(0,calculations):
            all_numbers[line_number][i]+=str(line[pointer:pointer+lengths[i]])
            pointer+=lengths[i]+1
        line_number+=1

for i in range(0,calculations):
    numbers = [ num[i] for num in all_numbers]
    length = lengths[i]
    operands = [ '' for i in range(0,length)]
    for k in range(0,length):
        for j in range(0,LIST_NUMBERS):
            operands[k]+=numbers[j][k]
    if i==1:
        print(operands)
    if operations[i] == "*":
        total = 1
        for operand in operands:
            total*=int(operand)
    else:
        total = 0
        for operand in operands:
            total += int(operand)
    count+=total
print(count)