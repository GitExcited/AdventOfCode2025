from pathlib import Path
INPUT_PATH = Path("../../inputs_shanvin/day_02.txt")

def find_invalid_inputs(line):
    result=0
    ranges=line.split(",")
    for i in ranges:
        current_range=i.split("-")
        print("Ranges:",current_range)
        lower_bound=current_range[0]
        upper_bound=current_range[1]
        for number in range(int(lower_bound), int(upper_bound) + 1):
            if len(str(number))%2==0:
                mid=len(str(number))//2
                if str(number)[:mid]==str(number)[mid:]:
                    result+=number
                    print(number)
    return result


def main():
    with open(INPUT_PATH, "r") as f:
        data = f.read()
        data=data.strip()
    result=find_invalid_inputs(data)
    print(result)

if __name__=="__main__":
    main()