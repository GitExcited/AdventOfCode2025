from pathlib import Path

INPUT_PATH = Path("../../inputs_shanvin/day_03.txt")

def find_largest_number(numbers):
    largest=0
    largest_index=0
    for char in range(len(numbers)-1):
        int_number=int(numbers[char])
        if largest<int_number:
            largest=int_number
            largest_index=char
    second_char=0
    for next in range(largest_index+1, len(numbers)):
        int_number_2=int(numbers[next])
        if second_char<int_number_2:
            second_char=int_number_2
    
    return (int(str(largest)+str(second_char)))


def find_largest_number_12(numbers):
    largest=0
    largest_index=0
    searching_end=11
    starting_index=-1
    result=""
    for i in range(searching_end, -1, -1):
        print("range:" +str(starting_index+1)+ " " + str(len(numbers)-i))
        for char in range(starting_index+1, len(numbers)-i):
            int_number=int(numbers[char])
            if largest<int_number:
                largest=int_number
                largest_index=char
        result+=str(largest)
        largest=0
        starting_index=largest_index
    return int(result)
    
    


def main():
    total_count=0
    with open(INPUT_PATH, "r") as f:
        for line in f:
            data=line.strip()
            result_line=find_largest_number_12(data)
            print(result_line)
            total_count+=result_line
    print (total_count)
        

if __name__=="__main__":
    main()