def count_xmas(filename):
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f.readlines()]
    
    rows, cols = len(grid), len(grid[0]) if grid else 0
    target = 'XMAS'
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    
    def dfs(r, c, index):
        if index == len(target):
            return 1
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != target[index]:
            return 0
        total = 0
        for dr, dc in directions:
            total += dfs(r + dr, c + dc, index + 1)
        return total
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                count += dfs(r, c, 1)
    
    return count

if __name__ == "__main__":
    filepath = 'input_Data/day_4.txt'
    total = count_xmas(filepath)
    print(f"Total 'XMAS' found: {total}")