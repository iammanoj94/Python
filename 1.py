import random

health = 50
difficulty = 1
print(health)
potion = int(random.randint(10, 50) / difficulty)
health = health + potion
print(health)
