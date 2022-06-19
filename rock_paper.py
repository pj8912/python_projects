import random

def play():
    user = input("What's your choice? 'r'->rock, 'p'->paper, 's'->scissor \n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie'
    if is_win(user, computer):
        return 'You Won'
    return 'You Lost!!'


def is_win(player, op):
    if(player == 'r' and op == 's') or (player == 's' and o == 'p') or (player == 'p' and op == 'r'):
        return True


print(play())

