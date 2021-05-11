"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dynasty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition 
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors. 
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
import random

N_GAMES = 3


def main():

    for x in range(N_GAMES):
        player_move = human_choice()
        ai_move = ai_choice()
        
        winner = get_winner(ai_move, player_move)
        print(winner + " wins!")
        print('')
    points = score(winner)
    print("Score: " + str(points))


def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')
    

def ai_choice():
    ran_number = random.randint(0,2)
    choices = ['scissors','paper','rock']
    ai_play = choices[ran_number]
    return ai_play


def human_choice():
    while True:
        player_choice = input("Please enter your choice: ")
        if is_valid_move(player_choice):
            return player_choice
        else:
            print("Invalid choice!")


def is_valid_move(move):
    if move == 'rock':
        return True
    elif move == 'scissors':
        return True
    elif move == 'paper':
        return True
    else:
        return False


def get_winner(ai_choice, player_choice):
    if ai_choice == player_choice:
        return "Noone"
    elif ai_choice == 'rock':
        if player_choice == 'scissors':
            return 'ai'
        return 'human'
    elif ai_choice == 'paper':
        if player_choice == 'rock':
            return 'ai'
        return 'human'
    elif ai_choice == 'scissors':
        if player_choice == 'paper':
            return 'ai'
        return 'human'
        

def score(winner):
    score = 0
    if winner == 'human':
        score += 1
    elif winner == 'ai':
        score -= 1
    else:
        score += 0    
    return score



if __name__ == '__main__':
    main()
