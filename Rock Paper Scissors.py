import random
user_score = 0
comp_score = 0
# LOOPING
for i in range(10):
    # PLAYERS PLAY
    user_input = int(input("0-Rock\n1-Paper\n2-Scissors\n"))
    if user_input == 0:
        print('You played - Rock')
    elif user_input == 1:
        print('You played - Paper')
    elif user_input == 2:
        print('You played - Scissors')
    # COMPUTERS PLAY
    computer = random.randint(0, 2)
    if computer == 0:
        print('Computer played - Rock')
    elif computer == 1:
        print('Computer played - Paper')
    elif computer == 2:
        print('Computer played - Scissors')
    if user_input > 2 or user_input < 0:
        print("Invalid Input")
    # SCORE
    else:
        if user_input == computer:
            user_score = user_score
            comp_score = comp_score
        elif (user_input == 0 and computer == 1) or (user_input == 1 and computer == 2) or (user_input == 2 and computer
                                                                                            == 0):
            comp_score += 1
            user_score = user_score
        elif (user_input == 1 and computer == 0) or (user_input == 2 and computer == 1) or (user_input == 0 and computer
                                                                                            == 2):
            comp_score = comp_score
            user_score += 1
    print('\n', user_score, comp_score, '\n')
# MOMENT OF TRUTH
if user_score > comp_score:
    print('You Win :)')
elif user_score < comp_score:
    print('You Lose :(')
elif user_score == comp_score:
    print('Score Tied!')
