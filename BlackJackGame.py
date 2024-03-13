import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []


def looping():
    a = 0
    for i in range(0, 4):
        i = random.choice(cards)
        if a == 0 or a == 2:
            player_cards.append(i)
        elif a == 1 or a == 3:
            computer_cards.append(i)
        a = a + 1


Game_on = True


def check_winner():
    if sum(computer_cards) > sum(player_cards):
        print(f"Computer's cards are: {computer_cards}")
        print("You lose")
    elif sum(computer_cards) < sum(player_cards):
        print(f"Computer's cards are: {computer_cards}")
        print("You win")


while Game_on:
    continue_game = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    os.system('cls')
    if continue_game == "y":
        print(logo)
        looping()
        print(f"your cards {player_cards}")
        print(f"Computers first card {computer_cards[0]}")
        z = True
        while z == True:
            ask = input("Type 'y' to get another card, type 'n' to pass: ")
            if ask == "y":
                x = random.choice(cards)
                player_cards.append(x)
                print(player_cards)
                if sum(player_cards) <= 21:
                    continue
                elif sum(player_cards) > 21:
                    print("Your sum went over 21, you lose.")
                    break
            else:
                if sum(computer_cards) >= 17:
                    check_winner()
                else:
                    x = random.choice(cards)
                    computer_cards.append(x)
                    if sum(computer_cards) > 21:
                        print(f"Computer's cards are: {computer_cards}")
                        print("You win.")
                    else:
                        check_winner()
                z = False
        player_cards.clear()
        computer_cards.clear()
    else:
        Game_on = False
