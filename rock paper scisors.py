import random
import time

options = ["rock", "paper", "scissors"]

player_win = 0
bot_win = 0

while True:
    user_input = input("press anything/enter to play or q (to quit): ").lower
    if user_input == "q":
        quit()
    else:
        user_choice = input("chose 0: rock, 1: paper ,2: scissors: ")
        if int(user_choice) > 2 or int(user_choice) < 0:
            print("wrong choices, chose 0: rock, 1: paper ,2: scissors")
            continue
        user_choice = options[int(user_choice)]
        if user_choice not in options:
            print("wrong choices, chose 0: rock, 1: paper ,2: scissors")
            continue
        else:
            random_num = random.randint(0, 2)
            bot_choice = options[random_num]
            print(f"THE BATTLE STARTS!!!!: {user_choice} vs {bot_choice}")
            if user_choice == bot_choice:
                print("none of you win, try again")
            if user_choice == options[0] and bot_choice == options[1]:
                bot_win += 1
                print("the bot won")
                print(f"your score: {player_win} and bot score: {bot_win}" )
            if user_choice == options[1] and bot_choice == options[0]:
                player_win += 1
                print("you won")
                print(f"your score: {player_win} and bot score: {bot_win}" )
            if user_choice == options[0] and bot_choice == options[2]:
                player_win += 1
                print("you won")
                print(f"your score: {player_win} and bot score: {bot_win}" )
            if user_choice == options[2] and bot_choice == options[0]:
                bot_win += 1
                print("the bot won")
                print(f"your score: {player_win} and bot score: {bot_win}" )
            if user_choice == options[2] and bot_choice == options[1]:
                player_win += 1
                print("you won")
                print(f"your score: {player_win} and bot score: {bot_win}" )
            if user_choice == options[1] and bot_choice == options[2]:
                bot_win += 1
                print("the bot won")
                print(f"your score: {player_win} and bot score: {bot_win}" )
            if int(player_win) == 5  or int(bot_win) == 5:
                print("game is done")
