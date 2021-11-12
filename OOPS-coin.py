import random
class Pound:
    def __init__(self, rare = False):
        self.rare = rare
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.0
        self.colour = "red"
        self.weight = 2.25
        self.Heads = True

    def rust(self):
        self.colour = "Greenish"
    def flip(self):
        Toss = [True, False]
        result = random.choice(Toss)
        if result:
            self.Heads = True
        else:
            self.Heads = False
    
    def __del__(self):
        print("Coin Spent!!")
