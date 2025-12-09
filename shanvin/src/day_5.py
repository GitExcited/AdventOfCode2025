from pathlib import Path
INPUT_PATH = Path("../../inputs_shanvin/day_05.txt")

def sort_ranges(range_grid):
    range_grid=sorted(range_grid, key=lambda x: int(x.split('-')[0]))
    result=[range_grid[0]]
    for i in range(1, len(range_grid)):
        number1, number2=int(range_grid[i].split("-")[0]), int(range_grid[i].split("-")[1])
        last_range1, last_range2=int(result[-1].split("-")[0]), int(result[-1].split("-")[1])
        if number1<=last_range2:
            result[-1]=str(last_range1)+"-"+str(max(last_range2, number2))
        else:
            result.append(range_grid[i])
    return result
def check_in_range(expiration_grid, new_range):
    expiration_grid=sorted(expiration_grid, key=lambda x:int(x))
    index=0
    counter=0
    for i in range(len(expiration_grid)):
        current=int(expiration_grid[i])
        for j in range(index, len(new_range)):
            range1, range2=int(new_range[j].split("-")[0]), int(new_range[j].split("-")[1])
            if range1<=current<=range2:
                counter+=1
                if j>=1:
                    index=j-1
                print ("here")
                break
            if current<range1:
                break
    return counter

def main():
    with open(INPUT_PATH, "r") as f:
        switch=True
        range_grid=[]
        expiration_grid=[]
        for line in f:
            data=line.strip()
            if not data:
                switch=False
            if switch and data:
                range_grid.append(data)
            if not switch and data:
                expiration_grid.append(data)
        new_range=sort_ranges(range_grid)
        result=check_in_range(expiration_grid, new_range)
        print (result)


        

if __name__=="__main__":
    main()