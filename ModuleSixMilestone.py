# Joey Cassello

#Dictionary for all rooms in my Santa's Workshop Christmas Adventure text-based game

rooms = {
        'Entry Hall': {'West': 'Candy Cane Lane'},
        'Candy Cane Lane': {'North': 'Toy Workshop', 'East': 'Entry Hall'},
        'Toy Workshop': {'West': 'Gift Wrapping Room', 'East': 'Jingle Bells Hall', 'North': 'Sleigh Garage', 'South': 'Candy Cane Lane'},
        'Gift Wrapping Room': {'East': 'Toy Workshop'},
        'Jingle Bells Hall': {'West': 'Toy Workshop', 'North': 'Cookie Kitchen'},
        'Cookie Kitchen': {'South': 'Jingle Bells Hall'},
        'Sleigh Garage': {'South': 'Toy Workshop', 'East': 'Reindeer Stables', 'West': 'The Grinch Hideout'},
        'Reindeer Stables':{'West': 'Sleigh Garage'},
        'The Grinch Hideout':{'East': 'Sleigh Garage'}
    }

def game():
    current_room = 'Entry Hall'

    while current_room != 'exit':
        print(f'You are in the {current_room}.')
        direction = input('Enter a direction (North, South, East, West) to move or "exit" to quit: ').capitalize()

        if direction == 'Exit':
            current_room = 'exit'
            print('Existing the game. Goodbye!')
        elif direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print('Invalid direction! Please enter a valid direction.')

game()