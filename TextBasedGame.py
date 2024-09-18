#Joseph Cassello

rooms = {
        'Entry Hall': {'West': 'Candy Cane Lane'},
        'Candy Cane Lane': {'North': 'Toy Workshop', 'East': 'Entry Hall', 'item': 'Ornament'},
        'Toy Workshop': {'West': 'Gift Wrapping Room', 'East': 'Jingle Bells Hall', 'North': 'Sleigh Garage', 'South': 'Candy Cane Lane', 'item': 'Teddy Bear'},
        'Gift Wrapping Room': {'East': 'Toy Workshop', 'item': 'Doll'},
        'Jingle Bells Hall': {'West': 'Toy Workshop', 'North': 'Cookie Kitchen', 'item': 'Action Figure'},
        'Cookie Kitchen': {'South': 'Jingle Bells Hall', 'item': 'GingerBread House'},
        'Sleigh Garage': {'South': 'Toy Workshop', 'East': 'Reindeer Stables', 'West': 'The Grinch Hideout', 'item': 'Magic Bells'},
        'Reindeer Stables':{'West': 'Sleigh Garage', 'item': 'Toy Train'},
        'The Grinch Hideout':{'East': 'Sleigh Garage'}
    }


inventory = []

def show_instructions():
     print("Christmas Adventure Game")
     print("Collect 7 items to win the game, or avoid the mean Grinch.")
     print("Move commands: go North, go South, go East, go West")
     print("Add to Inventory: get 'item name'")

def show_status(current_room):
    current_room = current_room.title()
    print(f'You are in the {current_room}.')
    print(f'Inventory: {inventory}.')
    if 'item' in rooms[current_room]:
        print(f'You see a {rooms[current_room]["item"]}')
    print('----------------------')

def main():
    current_room = 'Entry Hall'

    show_instructions()
    while True:
        show_status(current_room)
        command = input('Enter your move: ').lower()

        if command.startswith('go'):
            direction = command.split()[1].capitalize()
            if direction in rooms[current_room]:
               current_room = rooms[current_room][direction]
            else:
                print('Invalid direction! Please enter a valid direction.')
        elif command.startswith('get'):
            item = ' '.join(command.split()[1:]).capitalize()
            if 'item' in rooms[current_room] and rooms[current_room]['item'].capitalize() == item:
                print(f'You picked up the {item}.')
                inventory.append(item)
                del rooms[current_room]['item']
                if len(inventory) == 7:
                    print("Congratulations! You have collected all items and saved Christmas!")
                    print("Thanks for playing! I hope you enjoyed!")
                    break
            else:
                print(f'There is no {item} in this room.')
        else:
            print('Invalid command! Please enter a valid command.')

        if current_room == "The Grinch Hideout":
            print('NOM NOM...GAME OVER!')
            print("Thanks for playing! I hope you enjoyed!")
            break

if __name__ == "__main__":
    main()




