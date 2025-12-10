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

def reverse_it(operations):
    total_sum=0
    little_list=[]
    operation=" "

    for i in range(len(operations[0])-2, -1, -1):
        if operations[0][i]==" " and operations[1][i]==" " and operations[2][i]==" " and operations[3][i]==" " and operations[4][i]==" ":
            little_list=[]
            operation=""
            continue
        little_number=""
        if operations[0][i]!=" ": 
            little_number+=(operations[0][i])
        if operations[1][i]!=" ":
            little_number+=(operations[1][i])
        if operations[2][i]!=" ":
            little_number+=(operations[2][i])
        if operations[3][i]!=" ":
            little_number+=(operations[3][i])
        little_list.append(int(little_number))
        if operations[4][i]!=" ":
            operation=operations[4][i]
        if operation=="+":
            sum_1=sum(little_list)
            total_sum+=sum_1
            operation=" "
            little_list=[]
        if operation=="*":
            sum_1=1
            for j in little_list:
                sum_1*=j
            total_sum+=sum_1
            operation=" "
            little_list=[]
    return total_sum





def main():
    with open(INPUT_PATH, "r") as f:
        operations=[]
        operations_p2=[]
        for line in f:
            data=line
            data_2=data.split()
            operations.append(data_2)
            operations_p2.append(list(data))
        
    # print (do_it(operations))
    print (reverse_it(operations_p2))
        

        

if __name__=="__main__":
    main()