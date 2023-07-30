# This program adds positive numbers and returns the final sum when
# the user enters a negative number or 0.

result = 0

print('To get the result, type 0 or a negative number.')
while True:

    number = float(input('input a positive number: '))
    if number <= 0:
        break
    else:
        result += number

print(f'Your total is: {result}.')
