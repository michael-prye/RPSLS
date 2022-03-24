from human import Human
from ai import Ai
import time
class Game:
    def __init__(self):
        pass
    def run_game(self):
        self.display_welcome()
        time.sleep(1)
        self.display_rules()

        wrong_input = False
        while wrong_input == False:
            user_input = (input('How many players 1 or 2: '))
            while user_input.isdigit() == False:
                user_input = input('Enter a valid number: ')
            user_input = int(user_input)
            if user_input == 1:
                wrong_input = True
                winner = self.single_player()
                self.display_winner(winner)
            elif user_input == 2:
                wrong_input = True
                winner = self.multiplayer()
                self.display_winner(winner)


    def display_welcome(self):
        print('------------------------------------------------------')
        print('-----Welcome to Rock Paper Scissors Lizard Spock------')
        print('------------------------------------------------------')

    def display_rules(self):
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper')
        print('--------------------------')

    def single_player(self):
        p1_wins = 0
        ai_wins = 0
        rounds = 0
        player_one = Human()
        player_ai = Ai()

        game_over = False

        while game_over == False:
            ai_gesture = player_ai.ai_gesture()
            p1_gesture = player_one.my_gesture()
            x = self.get_winner(p1_gesture, ai_gesture)
            if x == 1:
                p1_wins += 1
                rounds += 1
                print('---------')
                print("P1 wins")
                print('---------')
                if p1_wins == 2:
                    game_over = True
                    return 1
            elif x == 2:
                ai_wins += 1
                rounds += 1
                print('---------')
                print("AI wins")
                print('---------')
                if ai_wins == 2:
                    game_over = True
                    return 2

        
    def display_winner(self,p1):
        if p1 == 1:
            print('------------------------')
            print(f'Player 1 is the Winner')
        elif p1 == 2:
            print('------------------------------')
            print(f"You just got beat by a robot!")
        else:
            print('-------')
            print("Player 2 is the Winner")
            print('-------')

            
    def multiplayer(self):
        p1_wins = 0
        p2_wins = 0
        rounds = 0
        player_one = Human()
        player_two = Human()
        game_over = False
        while game_over == False:
            p1_gesture = player_one.my_gesture()
            p2_gesture = player_two.my_gesture()
            x = self.get_winner(p1_gesture, p2_gesture)
            if x == 1:
                p1_wins += 1
                rounds += 1
            if p1_wins == 2:
                    game_over = True
                    return 1
            elif x == 2:
                p2_wins += 1
                rounds += 1
                print('-------')
                print("P2 wins")
                print('-------')
                if p2_wins == 2:
                    game_over = True
                    return 3
            else:
                rounds += 1 
        
        if p1_wins > p2_wins:
            print('-----------------------')
            print(f'Player 1 is the Winner')
        else:
            print('------------------------')
            print(f"Player 2 is the Winner!")

    def get_winner(self, p1,p2):
        if p1 == p2:
            return 0
        if p1 == 'rock' and (p2 == 'scissors' or p2 == 'lizard'):
            return 1
        elif p1 == 'scissors' and (p2 == 'paper' or p2 == 'lizard'):
            return 1
        elif p1 == 'paper' and (p2 == 'rock' or  p2 == 'spock'):
            return 1
        elif p1 == 'lizard' and (p2 == 'spock' or p2 == 'paper'):
            return 1
        elif p1 == 'spock' and (p2 == 'scissors' or p2 == 'rock'):
            return 1
        else:
            return 2
        

# test = Game()
# print(test.get_winner('spock', 'rock'))

# Rock crushes Scissors 
# Rock crushes Lizard 
# Scissors cuts Paper 
# Scissors decapitates Lizard 
# Paper covers Rock 
# Paper disproves Spock 
# Lizard poisons Spock 
# Lizard eats Paper
# Spock smashes Scissors 
# Spock vaporizes Rock