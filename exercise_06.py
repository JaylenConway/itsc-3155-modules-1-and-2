#Members: Manav M., Michael, Dylan D.
row = int(input('Enter a row num from 1 to 5: '))
col = int(input('Enter a col num from 1 to 5: '))

grid = [[0 for _ in range(5)] for _ in range(5)]

grid[row-1][col-1] = 1

for i in range(5):
    print(' ' + str(([grid[i][j] for j in range(5)])))  