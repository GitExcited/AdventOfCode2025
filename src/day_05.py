from  pathlib import Path

INPUT_PATH = Path("../inputs/day_05.txt")
#Theres 192 inputs of ranges
#from 194 to end its the actual digits
INPUT_LENGTH = 192
ranges= []
digits = []
with open(INPUT_PATH)  as file:
    i = 0
    for line in file:
        if i<INPUT_LENGTH:
            ranges.append(line.rstrip())

        elif i == INPUT_LENGTH:
            pass
        else:
            digits.append(line.rstrip())
        i += 1

# PART I
# count = 0
# for value in digits:
#     for bound in ranges:
#         bar = bound.find('-')
#         start = int(bound[:bar])
#         end = int(bound[bar+1:])
#         if start <= int(value) <= end:
#             count+=1
#             break

#PART II
count = 0
def get_start(bound:str)->int:
    return int(bound[:bound.find('-')])
def get_end(bound:str)->int:
    return int(bound[bound.find('-')+1:])

#Sort ranges first
ranges.sort(key=get_start)
previous_end = 0
for r in ranges:
    start = get_start(r)
    end = get_end(r)
    if previous_end >= end:
        continue
    if previous_end >= start:
        start = previous_end+1
    count += end-start+1
    previous_end = end

print(count)
