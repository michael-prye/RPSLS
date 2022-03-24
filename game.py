import time
from human import Human
from ai import Ai

class Game:
    def __init__(self):
        pass
    def run_game(self):
        self.display_welcome()
        time.sleep(1)
        self.display_rules()

        wrong_input = False
        user_input = (input('Type 1: for PvC, 2: PvP, or 3: CvC: '))
        while wrong_input == False:
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
            elif user_input == 3:
                wrong_input = True
                winner = self.bot_vs_bot()
                self.display_winner(winner)
            elif user_input < 0 or user_input > 3:
              user_input = input('Enter a valid number: ')



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
        player_one = Human()
        player_one.get_name()
        ai_1 = Ai()
        ai_1.get_name()
        game_over = False
        while game_over == False:
            ai_gesture = ai_1.ai_gesture()
            p1_gesture = player_one.my_gesture()
            x = self.get_winner(p1_gesture, ai_gesture)
            if x == 1:
                p1_wins += 1
                print('---------')
                print(f"{p1_gesture} beat {ai_gesture}")
                print(f"{player_one.name} wins this round")
                print('---------')
                if p1_wins == 2:
                    game_over = True
                    return player_one.name
            elif x == 2:
                ai_wins += 1
                print('---------')
                print(f"{ai_gesture} beat {p1_gesture}")
                print(f"{ai_1.name} wins this round")
                print('---------')
                if ai_wins == 2:
                    game_over = True
                    return ai_1.name
            else:
                print('---------')
                print('Its a tie. Play again')
                print('---------')
    def display_winner(self,p1):
        print('------------------------')
        print(f'{p1} is the Winner') 
    def multiplayer(self):
        p1_wins = 0
        p2_wins = 0
        player_one = Human()
        player_two = Human()
        player_one.get_name()
        player_two.get_name()
        game_over = False
        while game_over == False:
            p1_gesture = player_one.my_gesture()
            p2_gesture = player_two.my_gesture()
            x = self.get_winner(p1_gesture, p2_gesture)
            if x == 1:
                p1_wins += 1
                print('---------')
                print(f"{p1_gesture} beat {p2_gesture}")
                print(f"{player_one.name} wins this round")
                print('---------')
            if p1_wins == 2:
                    game_over = True
                    return player_one.name
            elif x == 2:
                p2_wins += 1
                print('-------')
                print(f"{p2_gesture} beat {p1_gesture}")
                print(f"{player_two.name} wins this round")
                print('-------')
                if p2_wins == 2:
                    game_over = True
                    return player_two.name
            else:
                print('---------')
                print('Its a tie. Play again')
                print('---------') 
    def bot_vs_bot(self):
        ai_1_wins = 0
        ai_2_wins = 0
        ai_1 = Ai()
        ai_2 = Ai()
        ai_1.get_name()
        ai_2.get_name()
        game_over = False
        while game_over == False:
            time.sleep(2)
            ai_gesture = ai_1.ai_gesture()
            ai_2_gesture = ai_2.ai_gesture()
            x = self.get_winner(ai_gesture, ai_2_gesture)
            if x == 1:
                ai_1_wins += 1
                print('---------')
                print(f"{ai_gesture} beat {ai_2_gesture}")
                print(f"{ai_1.name} wins this round")
                print('---------')
                if ai_1_wins == 2:
                    game_over = True
                    return ai_1.name
            elif x == 2:
                ai_2_wins += 1
                print('---------')
                print(f"{ai_2_gesture} beat {ai_gesture}")
                print(f"{ai_2.name} wins this round")
                print('---------')
                if ai_2_wins == 2:
                    game_over = True
                    return ai_2.name
            else:
                print('---------')
                print('Its a tie. Play again')
                print('---------')
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