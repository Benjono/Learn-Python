import random
import re

def play():
    user = input("'r' for rock, 'p' for paper, 's' for sissors \n")
    computer = random.choice(['r','p','s'])

    if user==computer:
        return 'tie'
    
    if is_win(user,computer):
        return 'You Won!'

    return 'You Lost!'
    
def is_win(player, opponent):
    if (player == 'r' and opponent =='s') or (player == 's' and opponent=='p') \
        or (player=='p' and opponent=='r'):
        return True
    return False
print(play())