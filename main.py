import random
import math
from replit import clear
from art import logo
print(logo)
print("２０２０ ｜ ＠Ｃｍｌｏｈｒ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Start Screen
print("Welcome! ʕ•́ᴥ•̀ʔっ")
start_game = input("Press ENTER to play").lower()
if start_game == "\n":
    clear()

player_hand = []
dealer_hand = []



def game():
    print(logo)
    cont = True
    while cont:
        dealer_score = 0
        player_score = 0
#Card Dealing
        draw_card = random.choices(cards)
        player_hand = random.choices(cards) * 2

#Score Calculating
        player_score = sum(player_hand)
        print(f"Your hand: {player_hand}, score: {player_score}")

#DOA Hands
        if player_score > 21:
            print("Player Bust! (╥︣﹏᷅╥) Dealer Wins!")
            if input("Play again? Type 'y' or 'n':\n> ").lower() == "y":
                game()  
            else:
                cont = False
                clear()

        dealer_hand = random.choices(cards)
        dealer_score = sum(dealer_hand)
        print(f"Dealer hand: {dealer_hand}, score: {dealer_score}")
        
        if dealer_score > 21:
            print("Dealer Bust! (✿◠‿◠) Player Wins!")
            print(f"Dealer hand: {dealer_hand}, score: {dealer_score}")
            if input("Play again? Type 'y' or 'n':\n> ").lower() == "y":
                game()  
            else:
                cont = False
                clear()
            
        if player_score and dealer_score < 21:
            hit_stand = input("Type 'y' to Hit or 'n' to Stand.\n> ").lower()

#Player Hit Stand Conditions
        if hit_stand == "y":
            print("Player Hits")
            player_hand = player_hand + draw_card
            player_score = sum(player_hand)
            print(f"Your hand: {player_hand}, score: {player_score}")
        if player_score > 21:
            print("Player Bust! (╥︣﹏᷅╥) Dealer Wins!")
            
            
        if hit_stand == "n":
            print("Player Stands")

#Dealer Hit or Stand Condition  
        while dealer_score <= 17:
            print("Dealer Hits")
            dealer_hand = dealer_hand + draw_card
            dealer_score = sum(dealer_hand)
            print(f"Dealer hand: {dealer_hand}, Score: {dealer_score}")

            if dealer_score > 17:
                print("Dealer Stands") 
                break

##############RULES##############
#PLAYER WINS
        if player_score > dealer_score and player_score <= 21:
            print("Player Wins! ᕙ(^▿^-ᕙ)")
            
#DEALER WINS        
        if dealer_score > player_score and dealer_score <= 21:
            print("Dealer Wins! (╥︣﹏᷅╥)") 
               
#BUST CONDITIONS
        if player_score > 21:
            print("Player Bust! (╥︣﹏᷅╥) Dealer Wins!")
        if dealer_score > 21:
            print("Dealer Bust! (✿◠‿◠) Player Wins!")

#DRAW
        if player_score == dealer_score:
            print("Draw! (☉̃ₒ☉)") 

#Restarts or Quits Game            
        if input("Play again? Type 'y' or 'n':\n> ").lower() == "y":
            game()  
        else:
            cont = False
            clear()
                 
game()
