def hasDigits(string):
    return any(char.isdigit() for char in string)

def sumList(list):
    for item in list:
        item = int(item)
    return sum(list)

def getCoordinates(filename):
    with open(filename,"r") as file:
        lines = [line for line in file]
    finalList = []
    for line in lines:
        first,second = -1,-1
        if hasDigits(line):
            for item in line:
                if item.isdigit() and first == -1:
                    first = str(item)
                elif item.isdigit() and second != -1:
                    second = str(item)
                elif second == -1:
                    second = first
            
            # \final = first + second
            finalList.append(str(first)+str(second))


    print(sumList(finalList))


getCoordinates("Day1\part1in.txt")
# getCoordinates("Day1\part1in.txt")

            
                


        




# print(lines[1])