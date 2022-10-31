number = int(input("Enter number : ")) # 


for x in range(number, 0, -1): # n до какого числа идёт колонка, 0 до которого столбика идём,  -2 сколько отнимаем с колонке
    for num in range(x,0, -1):# 1 с которого єлемента начнём, х которым закончим
        print(num, end=' ')
    print("")