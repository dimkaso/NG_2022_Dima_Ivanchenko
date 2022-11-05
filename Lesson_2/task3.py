number = int(input("Enter number : ")) # 


for x in range(number, 0, -1): # n to what number the column goes, 0 to which column we go, -2 how much we subtract from the column
    for num in range(x,0, -1):# 1 with which element we will start, x with which we will end
        print(num, end=' ')
    print("")