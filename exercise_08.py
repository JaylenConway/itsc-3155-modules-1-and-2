#Members: Manav M., Michael, Dylan D.
numbers = []

for i in range(10):
    num = int(input('Enter number ' + str(i + 1) + ': '))
    numbers.append(num)

unique = []
for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)

print("Original List: " + str(numbers))
print("Numbers that appear once: " + str(unique))