#Members: Manav M., Michael, Dylan D.
first_list = []
for i in range(5):
    num = int(input('Enter a number for the first list: '))
    first_list.append(num)

second_list = []
for i in range(5):
    num = int(input('Enter a number for the seconf list: '))
    second_list.append(num)

common_list = list(set(first_list) & set(second_list))

print('First List: ' + str(first_list))
print('Second List: ' + str(second_list))
print('Common List: ' + str(common_list))