#Members: Manav M., Michael, Dylan D.
number = input('Enter an integer greater than 1: ')
num = int(number)
start = 0

while start <= num:
    cube = str(start*start*start)
    start = str(start)
    print('The cube of ' + start + ' is ' + cube)
    start = int(start) + 1