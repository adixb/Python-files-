def AddNumber(x, y):
    sum_result = x + y
    print("Sum is:", sum_result)

def diffNumber(x, y):
    ans = abs(x - y)  # Absolute value ignores the negative sign
    print("Difference is:", ans)

def multiply(x, y):
    mul = x * y
    print("Product is:", mul)

def divide(x, y):
    if y != 0:
        div = x / y
        print("Quotient is:", div)
    else:
        print("Cannot divide by zero!")

while True:
    number_one = float(input('Enter your first number: '))
    last_number = float(input("Enter your last number: ")) 

    options = int(input("Enter any of the following options to calculate your result\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

    match options:
        case 1:
            AddNumber(number_one, last_number)
        case 2:
            diffNumber(number_one, last_number)
        case 3:
            multiply(number_one, last_number)
        case 4:
            divide(number_one, last_number)
        case _:
            print('Wrong option entered') 

    prompt = input("Do you wish to continue (y/n)? ")
    if prompt.lower() != 'y':
        break
