#Members: Manav M., Michael, Dylan D.
user_string = input('Enter a string: ')

chars = list(user_string)

split = [chars[i:i+3] for i in range(0, len(chars), 3)]

print(str(split))