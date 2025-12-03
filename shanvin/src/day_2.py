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

def find_invalid_inputs_p2(line):
    result=0
    ranges=line.split(",")
    for i in ranges:
        current_range=i.split("-")
        print("Ranges:",current_range)
        lower_bound=current_range[0]
        upper_bound=current_range[1]
        for number in range(int(lower_bound), int(upper_bound) + 1):
            number=str(number)
            divisor = len(number) // 2
            while divisor>=1:
                yes_flag=False
                if len(number)%divisor==0:
                    yes_flag=True
                    substring=number[0: divisor]
                    for j in range(divisor,len(number),divisor):
                        current_string=number[j: j+divisor]
                        if current_string!=substring:
                            yes_flag=False
                            break
                if yes_flag and len(number) > divisor:
                    result+=int(number)
                    break
                divisor-=1
    return result
def main():
    with open(INPUT_PATH, "r") as f:
        data = f.read()
        data=data.strip()
    result=find_invalid_inputs_p2(data)
    print(result)

if __name__=="__main__":
    main()