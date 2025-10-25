# 09/25/25 Moustapha Bah
# Lab 5 Pick Up Sticks Game

sticks_left = 13
current_turn = 0
players = ['Player 1', 'Player 2'] 
print("Welcome to Pick Up Sticks!")
print('Each player takes turns picking up 1 to 4 sticks from a pile of 13 sticks.')
print()
print('Whoever picks up the last stick wins the game.')
print(f'There are {sticks_left} sticks left.')
print() #empty prints for space betweens outputs
while sticks_left > 0:
    current_player_index = current_turn % len(players)
    current_player = players[current_player_index]
    # equations to alternate between players
    print(f"{current_player}'s turn.")
    sticks = int(input(f'{current_player}, how many stick(s) will you take?'))
   
    if sticks < 1 or sticks > 4 or sticks > sticks_left:
        # validation for number of sticks taken
        print(f"You can't take {sticks} sticks. Try again.")
        continue
    else:
        sticks_left = sticks_left - sticks
        current_turn += 1
        print() #empty print for space between outputs
        print(f'There are {sticks_left} sticks left.')
        # update for sticks left and next player's turn

    if sticks_left == 0:
        print(f'There are {sticks_left} sticks left.')
        print(f"{current_player} wins!")
        break
    #program ends when there are no sticks left and declares the winner




    
    
    
    
    

