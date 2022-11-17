value_for_the_pyramid = int(input("Enter number : ")) # 


for columns in range(value_for_the_pyramid, 0, -1): # n to what number the column goes, 0 to which column we go, -2 how much we subtract from the column
    for row in range(columns,0, -1):# 1 with which element we will start, x with which we will end
        print(row, end=' ')
    print("")