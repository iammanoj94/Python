Films = {
    "Avatar": [6, 3],
    "Bahubali": [12, 4],
    "Rrr": [18, 2],
    "sahoo": [16, 7]
    }

while True:
    choice = input("what film you wanted to watch ?:").strip().title()
    if choice in Films:
        age = int(input("How old are you?:").strip())
        #Check user Age
        if age >= Films[choice][0]:
            # check seat availability
            if Films[choice][1] >= 1:
                print("Enjoy the Film :)")
                Films[choice][1] = Films[choice][1] - 1
            else:
                print ("sorry seats are over :(" )
        else:
             print("Sorry!! you are not old enough to watch this film")
    else:
        print("We dont have film {} here".format(choice))
        
    
