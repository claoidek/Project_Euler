# Solves all the sudoku puzzles located in external_files/096_sudoku.txt and
# returns the sum of the three digit numbers in the top row of the first box of
# each puzzle

# Uses backtracking to solve the puzzles, described here:
# https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking
# It's pretty slow but improving it would involve implementing an entirely
# different algorithm so this will do for now

from time import clock

def get_grid(grid_number):
    new_grid = list(lines[grid_number*10-9:grid_number*10])
    for i in range(9):
        new_grid[i] = [int(s) for s in new_grid[i]]
    return new_grid

def get_row(i,grid):
    return grid[i]

def get_column(i,grid):
    return [row[i] for row in grid]

def get_box(i,grid):
    output = []
    column_start = (i%3)*3
    row_start = (i/3)*3
    output.extend(grid[row_start][column_start:column_start+3])
    output.extend(grid[row_start+1][column_start:column_start+3])
    output.extend(grid[row_start+2][column_start:column_start+3])
    return output

def get_box_num(row_num,column_num):
    row_third = row_num/3
    column_third = column_num/3
    return row_third*3 + column_third

def cell_to_row_column(cell):
    return cell/9,cell%9

def row_column_to_cell(row_num,column_num):
    return row_num*9+column_num

def check_set(group):
    no_zeroes = [value for value in group if value != 0]
    if len(no_zeroes) != len(set(no_zeroes)):
        return False
    return True

def check_validity(grid,cell_num):
    row_num,column_num = cell_to_row_column(cell_num)
    if not check_set(get_row(row_num,grid)):
        return False
    if not check_set(get_column(column_num,grid)):
        return False
    box_num = get_box_num(row_num,column_num)
    if not check_set(get_box(box_num,grid)):
        return False
    return True

def solve(grid):
    non_fixed = []
    index = 0
    for row_num,row in enumerate(grid):
        for column_num,column in enumerate(row):
            if column == 0:
                non_fixed.append(row_column_to_cell(row_num,column_num))

    while index < len(non_fixed):
        cell_num = non_fixed[index]
        row_num,column_num = cell_to_row_column(cell_num)
        if grid[row_num][column_num] == 9:
            grid[row_num][column_num] = 0
            index -= 1
        else:
            grid[row_num][column_num] += 1
            if check_validity(grid,cell_num):
                index += 1

start = clock()

with open("external_files/096_sudoku.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

num_grids = 50
grid_number = 1
total = 0

for grid_number in range(1,num_grids+1):
    grid = get_grid(grid_number)
    solve(grid)
    total += grid[0][0]*100 + grid[0][1]*10 + grid[0][2]

end = clock()

print total
print "Time taken: ", end-start, " s"
