from pathlib import Path
INPUT_PATH = Path("../../inputs_shanvin/day_09.txt")



def largest_area(coordinates):
    coordinates.sort(key=lambda x: x[0])
    max_area=0
    for i in range(len(coordinates)):
        for j in range(len(coordinates)-1, -1, -1):
            length=coordinates[j][0]-coordinates[i][0]+1
            height=coordinates[j][1]-coordinates[i][1]+1
            area=height*length
            if area>max_area:
                max_area=area
                small_x=coordinates[i][0]
                big_x=coordinates[j][0]
                small_y=coordinates[i][1]
                big_y=coordinates[j][1]
    for i in range(len(coordinates)):
        x, y = coordinates[i][0], coordinates[i][1]
        if x<small_x:
            if coordinates[i-1][0]==x or coordinates[i+1][0]==x:
                
            
    return max_area
def largest_area_P2(coordinates):
    max_x= min_x=coordinates[0][0]
    max_x_corresponding=min_x_corresponding=coordinates[0][1]
    max_y= min_y=coordinates[0][1]
    max_y_corresponding=min_y_corresponding=coordinates[0][0]
    for i in range(len(coordinates)):
        if coordinates[i][0]<min_x:
            min_x=coordinates[i][0]
            min_x_corresponding=coordinates[i][1]
        if coordinates[i][1]<min_y:
            min_y=coordinates[i][1]
            min_y_corresponding=coordinates[i][0]
        if coordinates[i][0]>max_x:
            max_x=coordinates[i][0]
            max_x_corresponding=coordinates[i][1]
        if coordinates[i][1]>max_y:
            max_y=coordinates[i][1]
            max_y_corresponding=coordinates[i][0]
    width1 = max_x - min_x + 1
    height1= max_x_corresponding- min_x_corresponding +1
    width2= max_y - min_y+1
    height2= max_y_corresponding - min_y_corresponding+1
    area1 = width1*height1
    area2=width2*height2
    return max(area1, area2)
            
def main():
    with open(INPUT_PATH, "r") as f:
        coordinates=[]
        for line in f:
            data=line.strip().split(",")
            data=[int(element) for element in data]
            coordinates.append(data)
    result=largest_area_P2(coordinates)
    print (result)
            
if __name__=="__main__":
    main()