first_num = int(input("Enter first number : "))
oper = input("Select Operators(+, -, *, /) : ")
second_num = int(input("Enter second number : "))

def basic_calculator():
    if oper == '+':
        print("The answer is" , first_num + second_num)
    elif oper == '-':
        print("The answer is" , first_num - second_num)
    elif oper == '*':
        print("The answer is" , first_num * second_num)
    elif oper == '/':
        print("The answer is" , first_num / second_num)
    else:
        print("There is no such operator!")

basic_calculator()