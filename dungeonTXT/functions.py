from os import system, name
from dungeon import has_key

# Clears console log every cicle


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def update_coordinates(user_input, coordinates):  # Player moving function
    first_coordinates = [coordinates[0], coordinates[1]]
    player_position = coordinates

    if user_input == 'north':
        player_position[1] += 1
    elif user_input == 'east':
        player_position[0] += 1
    elif user_input == 'south':
        player_position[1] -= 1
    elif user_input == 'west':
        player_position[0] -= 1

    if in_boundaries(player_position):  # If next position will be in the boundaries allow to move
        if (player_position == [-1, 0] or player_position == [0, -1]) and not has_key():
            return first_coordinates, False, False
        else:
            return player_position, True, True
    else:  # If next position is not in the boundaries, return current position
        return first_coordinates, False, True

# Check if next position is in dungeon area


def in_boundaries(next_position):  # Cheking if given coordinates have a "room"
    allowed = [[-1, -1], [-1, 0], [0, -1], [0, 0], [1, 0], [1, 1], [2, 0]]

    if next_position in allowed:
        return True
    else:
        return False
