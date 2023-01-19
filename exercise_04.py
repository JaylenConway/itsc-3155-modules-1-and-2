#Members: Manav M., Michael, Dylan D.
n = int(input('Enter a number: '))

numbers = []

for i in range(n):
    float_num = float(input("Enter number " + str(i+1) + ": "))
    numbers.append(float_num)

print('List: '+ str(numbers))
print('Average: '+ str(sum(numbers)/n))