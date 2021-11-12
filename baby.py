from random import choice
questions = ["why is earth spherical?", "why am i born?", "what is that?", "why is ur alive?"]

answer = input(choice(questions)).strip().lower()

while answer != "just because":
    answer = input("why? ").strip().lower()
print("Ohh okay..")

    
