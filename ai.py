import random
from player import Player

class Ai(Player):
    def __init__(self):
        super().__init__()
    
    def ai_gesture(self):
      ai_choice = random.choice(self.gestures)
      print('-----------')
      return ai_choice