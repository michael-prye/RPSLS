from human import Human
from ai import Ai
class Game:
    def __init__(self):
        pass
    def run_game(self):
        self.display_welcome()
        self.display_rules()

        wrong_input = False
        while wrong_input == False:
            user_input = (input('How many players 1 or 2: '))
            while user_input.isdigit() == False:
                user_input = input('Enter a valid number: ')
            user_input = int(user_input)
            if user_input == 1:
                wrong_input = True
                self.single_player()
            elif user_input == 2:
                wrong_input = True
                self.multiplayer()

    def display_welcome(self):
        print('Welcome')
    def display_rules(self):
        print('Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper')
    def single_player(self):
        p1_wins = 0
        ai_wins = 0
        rounds = 0
        player_one = Human()
        player_ai = Ai()

        while rounds <=3 or p1_wins == 2 or ai_wins == 2:
            p1_gesture = player_one.my_gesture()
            ai_gesture = player_ai.ai_gesture()
            x = self.get_winner(p1_gesture, ai_gesture)
            if x == 1:
                p1_wins += 1
                rounds += 1
            elif x == 2:
                ai_wins += 1
                rounds += 1
            else:
                round += 1 
    def multiplayer(self):
        pass
    def get_winner(self, p1,p2):
        if p1 == p2:
            return 0
        if p1 == 'rock' and p2 == 'scissors' or p2 == 'lizard':
            return 1
        elif p1 == 'scissors' and p2 == 'paper' or p2 == 'lizard':
            return 1
        elif p1 == 'paper' and p2 == 'rock' or p2 == 'spock':
            return 1
        elif p1 == 'lizard' and p2 == 'spock' or p2 == 'paper':
            return 1
        elif p1 == 'spock' and p2 == 'scissors' or p2 == 'rock':
            return 1
        else:
            return 2
        

test = Game()
print(test.get_winner('rock', 'lizard'))

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