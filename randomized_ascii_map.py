import random

def generate_map(size_x, size_y):
    # Initialize the map with 'x' tiles, representing undetermined terrain
    # The '#' tiles represent the border of the map
    map_grid = [['x' if i != 0 and i != size_x - 1 and j != 0 and j != size_y - 1 else '#' for j in range(size_y)] for i in range(size_x)]

    # Define the symbols for different types of terrain:
    terrain_symbols = {
        'Road': '.',    # Represents a road
        'Grass': '^',   # Represents grass terrain
        'Water': '~',   # Represents water terrain
        'Empty': 'o'    # Represents empty terrain
    }

    def print_map(map_grid):
        for row in map_grid:
            print(''.join(row))

    def convert_empty_tiles():
        # Define the bias probabilities for each terrain type
        grass_bias = 0.3  # bias for grass
        water_bias = 0.1  # bias for water
        # empty_bias = 1 - grass_bias - water_bias

        for i in range(size_x):
            for j in range(size_y):
                if map_grid[i][j] == 'x':
                    # Randomly select terrain type based on bias probabilities
                    random_value = random.random()
                    if random_value < grass_bias:
                        map_grid[i][j] = terrain_symbols['Grass']
                    elif random_value < grass_bias + water_bias:
                        map_grid[i][j] = terrain_symbols['Water']
                    else:
                        map_grid[i][j] = terrain_symbols['Empty']


    # Find a random starting point for the road:
    possible_starts = {
        'north': [(0, j) for j in range(1, size_y - 1)],
        'south': [(size_x - 1, j) for j in range(1, size_y - 1)],
        'east': [(i, size_y - 1) for i in range(1, size_x - 1)],
        'west': [(i, 0) for i in range(1, size_x - 1)]
    }
    # possible_starts is a dictionary where each key represents a direction ('north', 'south', 'east', or 'west'), 
    # and the corresponding value is a list of possible starting positions within that direction.

    road_start = random.choice(random.choice(list(possible_starts.values())))
    # use random.choice(list(possible_starts.values())) to randomly select one of the lists of possible starting positions
    # use another random.choice() to select a specific starting position from the list

    # Set the starting tile of the road:
    map_grid[road_start[0]][road_start[1]] = terrain_symbols['Road']

    # Determine the direction of the starting tile:
    if road_start in possible_starts['north']:
        home = 'north'
    elif road_start in possible_starts['south']:
        home = 'south'
    elif road_start in possible_starts['east']:
        home = 'east'
    elif road_start in possible_starts['west']:
        home = 'west'

    # Extend the road entity:
    opposite_directions = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'} # Dictionary to define opposite directions
    direction = opposite_directions[home]  # The road always extends in the opposite direction on the first loop
    # Loop until the road entity reaches a border of the map:
    while True:
        # Extend the road in the chosen direction:
        if direction == 'south':
            road_start = (road_start[0] + 1, road_start[1])
        elif direction == 'north':
            road_start = (road_start[0] - 1, road_start[1])
        elif direction == 'east':
            road_start = (road_start[0], road_start[1] + 1)
        elif direction == 'west':
            road_start = (road_start[0], road_start[1] - 1)
        
        # Convert the next road tile to road terrain:
        map_grid[road_start[0]][road_start[1]] = terrain_symbols['Road']
        
        # Check if the road entity has reached a border, if so, break the loop:
        if road_start[0] == 0 or road_start[0] == size_x - 1 or road_start[1] == 0 or road_start[1] == size_y - 1:
            # = if the road start is at the top, bottom, left, or right edge of the map:
            break

        # Remove the home direction from the pool of possible directions to bias the road direction away from where it started:
        possible_directions = ['north', 'south', 'east', 'west']
        possible_directions.remove(home)

        # Choose a random direction from the possible directions
        direction = random.choice(possible_directions)

    # Convert empty tiles to grass, water, or empty terrain
    convert_empty_tiles()

    # Print the generated map
    print_map(map_grid)

# Set the size of the grid:
size_x = 15
size_y = 20

# Execute code:
generate_map(size_x, size_y)
