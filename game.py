
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
        pass
    def multiplayer(self):
        pass
test = Game()
test.run_game()