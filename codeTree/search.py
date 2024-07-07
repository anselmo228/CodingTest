def max_coins_in_subgrid(n, grid):
    max_coins = 0
    
    for i in range(n - 2):
        for j in range(n - 2):
            current_coins = sum(grid[i+k][j+l] for k in range(3) for l in range(3))
            max_coins = max(max_coins, current_coins)
    
    return max_coins

n = int(input().strip())
grid = [list(map(int, input().strip().split())) for _ in range(n)]

print(max_coins_in_subgrid(n, grid))
