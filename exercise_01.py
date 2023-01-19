#Members: Manav M., Michael, Dylan D.
grade = input('Enter a grade from 0 to 100: ')
grade = int(grade)

if grade >= 90:
    result = 'A'
elif grade >= 80 and grade < 90:
    result = 'B'
elif grade >= 70 and grade < 80:
    result = 'C'
elif grade >= 60 and grade < 70:
    result = 'D'
else:
    result = 'F'

print(result)
