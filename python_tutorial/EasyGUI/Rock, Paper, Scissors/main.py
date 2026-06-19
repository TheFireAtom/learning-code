import easygui
import random


names = ("Rock", "Paper", "Scissors")

player_score = 0
bot_score = 0

easygui.buttonbox(
    title="Test",
    msg="Something",
    choices=["Test"],
    images=["C:\Programming_stuff\learning-code\python_tutorial\EasyGUI\Rock, Paper, Scissors\assets\Hello_Kitty_Pink_GIF.gif"]
)

start = easygui.msgbox("Welcome to Rock, Paper, Scissors", ok_button="Okay")
if start is None:
    easygui.msgbox("Game cancelled.")
    exit()

def player_choice_func():
    player_choice = easygui.buttonbox(
        title="Rock, Paper, Scissors", 
        msg="Choose your weapon: ",
        choices=["Rock", "Paper", "Scissors"], 
        images=["assets/rock.gif", "assets/paper.gif", "assets/scissors.gif"]
    )
    
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

def play_round(player, bot_choice):
    global player_score, bot_score
    if player == bot_choice:
        player_score += 1
        bot_score += 1
        return "Tie!"
    elif (player == 1 and bot_choice == 3) or \
    (player == 2 and bot_choice == 1) or \
    (player == 3 and bot_choice == 2):
        player_score += 1
        return "Player wins!"
    # elif player or bot_choice is None:
    #     easygui.msgbox("Game cancelled.")
    #     exit()
    else:
        bot_score += 1
        return "Bot wins!"
    
    
# def determine_round_winner(rnd):
#     global player_score, bot_score  # Объявили ГРОМКО на входе!
#     if rnd == "Tie!":
#         player_score += 1
#         bot_score += 1
#         return 1, 1
#     elif rnd == "Player wins!":
#         player_score += 1  # Теперь Python знает, что это глобальная переменная
#         return 1, 0
#     elif rnd == "Bot wins!":
#         bot_score += 1  # И эта тоже
#         return 0, 1
    
def results():
    if player_score > bot_score:
        easygui.textbox("Player is winning this tour!")
    elif bot_score > player_score:
        easygui.textbox("Bot is winning this tour!")
    else: 
        easygui.textbox("Draw!")
    

# def three_rounds(player, bot):
#     player_score = 0
#     bot_score = 0
#     if game(player, bot) ==  "Tie!":
#         player_score += 1
#         bot_score += 1
#     elif game(player, bot) == "Player wins!":
#         player_score += 1
#     elif game(player, bot) == "Bot wins!":
#         bot_score += 1
#     return player_score, bot_score

for _ in range(3):

    player = player_choice_func()
    bot = bot_choice_func()
    if player is None: 
        easygui.msgbox("Game cancelled.")
        exit()
    play_round(player, bot)

results()



    # three_rounds(player, bot)
    
    







