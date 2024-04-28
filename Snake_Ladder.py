import random

def matrix(rows, columns):
    m = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * columns + j)
        m.append(row)
    return m

def dice():
    sides = 6
    roll_count = random.randint(1, sides)
    return roll_count

def player(current_position, roll_count):
    new_position = current_position + roll_count
    return new_position

def snake(player_position):
    if player_position == 6:
        player_position -= 4
    elif player_position == 12:
        player_position -= 5
    return player_position

def ladder(player_position):
    if player_position == 7:
        player_position += 2
    elif player_position == 11:
        player_position += 3
    return player_position

rows = 4
columns = 4
player_position = 0
result = matrix(rows, columns)

for row in result:
    print(row)

print("Play Snake and Ladders")
print("Snake is at 6 and 15")
print("Ladder is at 7 and 11")
print("Let the dice roll")

while True:
    user_input = input("Press 'Enter' to roll the dice or type 'exit' to end the game: ")
    
    if user_input.lower() == 'exit':
        break
    
    roll_result = dice()
    print("You rolled:", roll_result)

    player_position = player(player_position, roll_result)
    print("The player's position after moving:", player_position)

    if player_position == 15:
        print("Congratulations! You've reached position 15. You won!")
        break

    player_position = snake(player_position)
    print("The player's position after checking for snakes:", player_position)

    player_position = ladder(player_position)
    print("The player's position after checking for ladders:", player_position)

    if player_position > 15:
        print("Oops! You rolled too high. Try again.")
        player_position = 0

        player_position = snake(player_position)
        print("The player's position after checking for snakes:", player_position)

        player_position = ladder(player_position)
        print("The player's position after checking for ladders:", player_position)
