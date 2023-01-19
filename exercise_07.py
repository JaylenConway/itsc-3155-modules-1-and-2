#Members: Manav M., Michael, Dylan D.
numbers = []

while True:
    user_input = input('Enter a number or QUIT to quit: ')
    if user_input.upper() == 'QUIT':
        break
    else:
        numbers.append(int(user_input))

even_numbers = [x for x in numbers if x % 2 == 0]

print('All Nums: ' + str(numbers))
print('Even Nums: ' + str(even_numbers))
