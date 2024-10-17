num1 = int(input('Enter first integer: '))
num2 = int(input('Enter second integer: '))
op = input('Enter operator (+ - * /): ')

if op == '+':
    print(f'{num1} + {num2} =', num1 + num2)
elif op == '-':
    print(f'{num1} - {num2} =', num1 - num2)
elif op == '*':
    print(f'{num1} * {num2} =', num1 * num2)
elif op == '/':
    if num2 == 0:
        print(f'{num1} / 0 = ERROR: Cannot divide by zero')
    else:
        print(f'{num1} / {num2} =',num1 / num2)
else:
    print(f'{num1} {op} {num2} = Illegal operation')



