original = input('Enter a string: ')
lower = []
upper = []

for char in original:
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)

output = ''.join(lower) + ''.join(upper)
print(output)