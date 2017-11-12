def island_perimeter(grid):
    land_points = []
    row = 0
    #print "grid is " + str(len(grid))
    while row < len(grid):
        #print "grid row is " + str(len(grid[row]))
        col = 0
        while col < len(grid[row]):
            if grid[row][col] == 1:
                land_points.append((row, col))
            col += 1
        row += 1
    print land_points
    row = [0] * len(grid)
    col = [0] * len(grid)
    for i in land_points:
        row[i[0]] += 1
        col[i[1]] += 1
    print row
    print col
        

if __name__ == '__main__':
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    island_perimeter(grid)