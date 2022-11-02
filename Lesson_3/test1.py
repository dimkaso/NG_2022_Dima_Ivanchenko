#function to introduce
def namber(text):
    valueA = int(float(input(text)))
    return valueA


# functions for actions
def Sum(valueA,valueB ):
    return valueA + valueB
    
def Multiplication(valueA,valueB ):
    return valueA * valueB
    
def Degree(valueA,valueB ):
    return valueA ** valueB

def Minus(valueA,valueB ):
    return valueA - valueB

def Root(valueA,valueB ):
    import math
    return math.sqrt(valueA),math.sqrt(valueB)

def Division(valueA,valueB ):
    return valueA / valueB





#function to display values
def enterSum():
    print("Result sum = " + str(Sum(namber("ValueA = "),namber("ValueB ="))))


def enterMultiplication():
    print("Result Multiplication= " + str(Multiplication(namber("ValueA ="),namber("ValueB ="))))


def enterDegree():
    print("Result Degree= " + str(Degree(namber("ValueA ="),namber("ValueB ="))))


def enterMinus():
    print("Result Minus= " + str(Minus(namber("ValueA ="),namber("ValueB ="))))


def enterRoot():
    print("Result Root=" + str(Root(namber("ValueA ="),namber("ValueB ="))))


def enterDivision():
    print("Result Division =  " + str(Division(namber("ValueA ="),namber("ValueB ="))))

# function to clarify the conditions under which it goes
def main():
    operation = str(input("Choose operation(+,-,*,/,^,sqrt): "))
    if operation=="+":
        enterSum()
    if operation=="*":
        enterMultiplication()
    if operation=="^":
        enterDegree()
    if operation=="sqrt":
        enterRoot()
    if operation=="-":
        enterMinus()
    if operation=="/":
        enterDivision()

    else:
        print("No, only (+,-,*,/,^,sqrt) ")
main()