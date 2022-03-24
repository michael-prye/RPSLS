from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        
    def my_gesture(self):
        index = 0
        for gesture in self.gestures:
            print(f'for {gesture} enter {index}')
            index += 1

        wrong_input = False
        while wrong_input == False:
            user_input = (input('Which gesture would you like to use? '))
            while user_input.isdigit() == False:
                user_input = input('Enter a valid number: ')
            user_input = int(user_input)
            if user_input >= 0 and user_input < len(self.gestures):
                wrong_input = True
                return self.gestures[user_input]
            else:
                print("Number is out of range")

# # test = Human()
# print(test.my_gesture())
      