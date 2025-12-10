from pathlib import Path
INPUT_PATH = Path("../../inputs_shanvin/day_06.txt")

def do_it(operations):
    total_sum=0
    for i in range(len(operations[0])):
        number1=int(operations[0][i])
        number2=int(operations[1][i])
        number3=int(operations[2][i])
        number4=int(operations[3][i])
        if operations[4][i]=="+":
            sum=number1+number2+number3+number4
        elif operations[4][i]=="*":
            sum=number1*number2*number3*number4
        total_sum+=sum
    return total_sum





def main():
    with open(INPUT_PATH, "r") as f:
        operations=[]
        for line in f:
            data=line.strip()
            data=data.split()
            operations.append(data)
    print(len(operations[0]))
    print (do_it(operations))
        

        

if __name__=="__main__":
    main()