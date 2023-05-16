grid = [
    ['X', 'X', 'X', 'X', '.'],
    ['X', '.', '.', '.', '.'],
    ['X', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['X', 'X', '.', 'X', 'X']
]

# Assign tile numbers to each tile
grid_size = 5
tile_number = 0
tile_numbers = [[0] * grid_size for _ in range(grid_size)]
for row in range(grid_size):
    for col in range(grid_size):
        tile_numbers[row][col] = tile_number
        tile_number += 1

# Print the grid with tile numbers
for row in range(grid_size):
    for col in range(grid_size):
        print(grid[row][col], end=' ')
    print("  ", end='')
    for col in range(grid_size):
        print(tile_numbers[row][col], end=' ')
    print()

layouts = {}

minute = 0
while True:
    # Convert the grid back to a string representation
    layout = ''.join(''.join(row) for row in grid)

    # Check if the layout has been encountered before
    if layout in layouts:
        first_appearance_minute = layouts[layout]
        break

    # Store the current minute for the layout
    layouts[layout] = minute

    # Create a copy of the grid for updating
    new_grid = [row.copy() for row in grid]

    # Print the layout for the current minute
    print(f"\nMinute {minute}:\n")
    for row in range(grid_size):
        for col in range(grid_size):
            print(grid[row][col], end=' ')
        print()

    # Iterate over each tile in the grid
    for i in range(25):
        row, col = divmod(i, 5)
        adjacent_count = 0

        # Check the four adjacent tiles
        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            new_row, new_col = row + dr, col + dc

            # Skip if the adjacent tile is outside the grid
            if not (0 <= new_row < 5 and 0 <= new_col < 5):
                continue

            # Count the adjacent lifeforms
            if grid[new_row][new_col] == 'X':
                adjacent_count += 1

        # Update the tile based on the rules
        if grid[row][col] == 'X' and adjacent_count != 1:
            new_grid[row][col] = '.'
        elif grid[row][col] == '.' and adjacent_count in (1, 2):
            new_grid[row][col] = 'X'

    # Update the grid for the next minute
    grid = new_grid.copy()
    minute += 1

lifeform_score = sum(2 ** tile_num for tile_num, tile_value in enumerate(layout) if tile_value == 'X')
print("\nLifeform score:", lifeform_score)
print("Grid:")
for row in range(grid_size):
    for col in range(grid_size):
        print(grid[row][col], end=' ')
    print()
