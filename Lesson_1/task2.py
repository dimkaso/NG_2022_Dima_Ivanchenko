import math
while True:
    value_a = float(input("Enter A: "))
    value_b = float(input("Enter B: "))
    operation = str(input("Choose operation(+,-,*,/,^,sqrt): "))
    if operation=="+":
        print(f'A+B {value_a+value_b}')
    
    if operation=="-":
        print(f'A-B {value_a-value_b}')
    
    if operation=="*":
        print(f'A*B {value_a*value_b}')
    
    if operation=="/":
        print(f'A/B {value_a/value_b}')
    
    if operation=="^":
        print(f'A^2 {value_a**2}' )
        print(f'B^2 {value_b**2}' )
        
    if operation=="sqrt":
        print(f'sqrt A {int(math.sqrt(value_a))}' )
        print(f'sqrt B {int(math.sqrt(value_b))}' )   
    continue_ = str(input("Do you want to continue (Yes/No): "))
    if continue_=="No":
        break
