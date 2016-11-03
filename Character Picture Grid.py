#This one is give
grid = [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

#I have to print something like this
#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....
for a in range(len(grid[0])):
    for b in range(len(grid)):
        print(grid[b][a],end='')
    print('')
