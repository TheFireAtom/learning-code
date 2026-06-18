import easygui
import random

names = ("Rock", "Paper", "Scissors")

start = easygui.msgbox("Welcome to Rock, Paper, Scissors")
if start is None:
    easygui.msgbox("Game cancelled.")
    exit()

def player_choice_func():

    player_choice = easygui.buttonbox("Choose your element: ", title="Some words here", choices=(names[0], names[1], names[2]))
    
    if player_choice == names[0]:
        return 1
    elif player_choice == names[1]:
        return 2
    elif player_choice == names[2]:
        return 3
    elif player_choice is None:
        return None

def bot_choice_func():
    bot_choice = random.randint(1, 3)
    return bot_choice

def output(player, bot_choice):
    if player == bot_choice:
        return "Tie!"
    elif (player == 1 and bot_choice == 3) or \
    (player == 2 and bot_choice == 1) or \
    (player == 3 and bot_choice == 2):
        return "Player wins!"
    else:
        return "Bot wins!"
    
player = player_choice_func()
bot = bot_choice_func()

if player is None: 
    easygui.msgbox("Game cancelled.")
    exit()

print("Bot: ", bot)
print("Player", player)

print(output(player, bot))




