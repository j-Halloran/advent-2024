def is_xmas(grid, r, c):
    # We assume (r,c) is the center of a potential X-MAS pattern.
    # Check bounds first
    if r-1 < 0 or r+1 >= len(grid) or c-1 < 0 or c+1 >= len(grid[0]):
        return False
    
    center = grid[r][c]
    if center != 'A':
        return False
    
    # Positions of the diagonals
    # Main diagonal: top-left, center, bottom-right
    tl = grid[r-1][c-1]
    br = grid[r+1][c+1]
    # Off diagonal: top-right, center, bottom-left
    tr = grid[r-1][c+1]
    bl = grid[r+1][c-1]
    
    # Check if diagonals form MAS or SAM
    # Allowed sets for each diagonal: {'M', 'A', 'S'} with 'A' in the middle
    def valid_diagonal(a, mid, b):
        diag = a + mid + b
        return diag == "MAS" or diag == "SAM"
    
    return valid_diagonal(tl, center, br) and valid_diagonal(tr, center, bl)


if __name__ == "__main__":
    with open("input_data/day_4.txt") as f:
        grid = [list(line.strip()) for line in f if line.strip()]
        
    count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if is_xmas(grid, i, j):
                count += 1
    
    print(count)
