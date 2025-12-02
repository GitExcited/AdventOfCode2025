from pathlib import Path
import csv
from typing import List

INPUT_PATH = Path("../inputs/day_02.txt")
product_ids = []
with open(INPUT_PATH)  as file:
    reader = csv.reader(file)
    for row in reader:
        for el in row:
            product_ids.append(el)

def is_valid_id(_id:str) -> bool :
    #Assumption: if id is odd, it can't be a duplicate of 2 numbers: 313 is not an invalid id for example. 3113 is.
    length = len(_id)
    if length%2 != 0 :
        return True
    elif _id[0: length// 2] == _id[length//2:]:
        return False
    return True

def find_invalid(start:int, end:int)->List[int]:
    invalid= []
    for i in range(start, end+1):
        if not is_valid_id(str(i)):
            invalid.append(i)
    return invalid

sum = 0
for product_id in product_ids:
    both_ids = product_id.split("-")
    firstID = both_ids[0]
    lastID = both_ids[1]
    invalid_IDs =find_invalid(int(firstID),int(lastID))
    for invalid_id in invalid_IDs:
        sum+=invalid_id
 # PART 1
print("Part 1 Answer ⭐")
print(sum)
print("================")

# PART 2

def is_valid_id_2(_id:str)->bool:
    length_number = len(_id)
    #Begin checking digits [1] [12]  [123]
    for i in range(0,(length_number//2)+1):
        substring = _id[0:i]
        count = _id.count(substring)
        if i*count== length_number:
            return False
    return True

def find_invalid_2(start:int, end:int)->List[int]:
    invalid= []
    for i in range(start, end+1):
        if not is_valid_id_2(str(i)):
            invalid.append(i)
    return invalid
sum = 0
for product_id in product_ids:
    both_ids = product_id.split("-")
    firstID = both_ids[0]
    lastID = both_ids[1]
    invalid_IDs =find_invalid_2(int(firstID),int(lastID))
    for invalid_id in invalid_IDs:
        sum+=invalid_id
print("Part 2 Answer ⭐")
print(sum)
print("================")

# something = "1212"
# print(is_valid_id_2(something))
# print(something.count("123"))