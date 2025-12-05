from  pathlib import Path

INPUT_PATH = Path("../inputs/day_05.txt")
#Theres 192 inputs of ranges
#from 194 to end its the actual digits
ranges= []
digits = []
with open(INPUT_PATH)  as file:
    i = 0
    for line in file:
        if i<192:
            ranges.append(line.rstrip())

        elif i == 192:
            pass
        else:
            digits.append(line.rstrip())
        i += 1


valid_digits_dict = set()
for bound in ranges:
    bar = bound.find('-')
    start = int(bound[:bar])
    end = int(bound[bar+1:])
    for i in range (start,end+1):
        valid_digits_dict.add(i)
count = 0
for value in digits:
    if value in valid_digits_dict:
        count+=1

print(count)
