import random

health = 30
level = 3
portion = int(random.randint(30,100)/level)
print(portion)
health = (health + portion)
print(health)
