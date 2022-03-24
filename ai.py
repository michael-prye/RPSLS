import random
from player import Player

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.bot_names = ["Terminator", "I-Robot", "Iron Giant", "Alexa", "Johnny 5", "Siri"]
    
    def ai_gesture(self):
      ai_choice = random.choice(self.gestures)
      print('-----------')
      return ai_choice
