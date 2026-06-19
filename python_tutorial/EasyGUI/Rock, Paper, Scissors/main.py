import easygui
import random
import os 
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

rock_img_path = os.path.join(ASSETS_DIR, "rock.gif")
paper_img_path = os.path.join(ASSETS_DIR, "paper.gif")
scissors_img_path = os.path.join(ASSETS_DIR, "scissors.gif")

size = (64, 64)

img_rock = Image.open(rock_img_path).resize(size)
img_paper = Image.open(paper_img_path).resize(size)
img_scissors = Image.open(scissors_img_path).resize(size)

small_rock = os.path.join(ASSETS_DIR, "rock_small.gif")
small_paper = os.path.join(ASSETS_DIR, "paper_small.gif")
small_scissors = os.path.join(ASSETS_DIR, "scissors_small.gif")

img_rock.save(small_rock)
img_paper.save(small_paper)
img_scissors.save(small_scissors)

names = ("Rock", "Paper", "Scissors")
player_score = 0
bot_score = 0

# print("Current folder: ", os.getcwd())
# if os.path.exists(ASSETS_DIR + "assets"):
#     print("Path exist")
# else:
#     print("Path do not exist")

# easygui.buttonbox(
#     title="Test",
#     msg="Something",
#     choices=["Test"],
#     images=[rock_img_path]
# )

start = easygui.msgbox("Welcome to Rock, Paper, Scissors", ok_button="Okay")
if start is None:
    easygui.msgbox("Game cancelled.")
    exit()

def player_choice_func():
    player_choice = easygui.buttonbox(
        title="Rock, Paper, Scissors", 
        msg="Choose your weapon: ",
        choices=[], 
        images=[small_rock, small_paper, small_scissors]
    )
    
    if player_choice == small_rock:
        return 1
    elif player_choice == small_paper:
        return 2
    elif player_choice == small_scissors:
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
    easygui.textbox("Player score: ", text=str(player_score))
    easygui.textbox("Bot score: ", text=str(bot_score))
    if bot_score == 2 or player_score == 2:
        results()

results()
    
    







