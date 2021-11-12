import random

class Coin:
    def __init__(self, rare=False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)
        
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
        if self.is_rare:
            self.vaue = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.clour = self.rusty_colour
    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin Spent!")
   
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

class Pound(Coin):
    def __init__(self):
        data = { "original_value": 80,
                 "rusty_colour": "Black",
                 "clean_colour": "Gold",
                 "weight": 22.5,
                 }
        super().__init__(**data)

class Rupee(Coin):
    def __init__(self):
        data = { "original_value": 1,
                 "rusty_colour": "Yellowish",
                 "clean_colour": "Silver",
                 "weight": 11,
                 }
        super().__init__(**data)
