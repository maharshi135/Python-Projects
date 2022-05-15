import random

from numpy import true_divide 

def play():
    user = input("What's your choice? 'r' for rock, 'p' for peper and 's' for scissors\n" )
    computer = random.choice(['r','p','s'])
    print(f'computer has choose {computer}')
    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

print(play())