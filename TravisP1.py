known_users = ["Alice" , "Bob" , "Claire" , "Dan" , "Emma" , "Fred" , "Georgie" , "Harry"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input(" What is your name? :").strip().capitalize()
    if    name in known_users:
        print("name recognised")
        print("Helloo {}!!, WELCOME to Travis ".format(name))
        remove = input("Would you like to remove your name (y/n): ").lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem I didnt do anything :)")
        else:
            print("you have entered incorrect response :(")
        
    else:
        print("you are not a member".format(name))
        add_me = input("Do you want me to add to members list ? (y/n)").lower().strip()
        if add_me == "y":
            known_users.append(name)
            print("you are added {}".format(name))
        elif add_me == "n":
            print("No problem I didnt do anything :)")
        else:
            print("you have entered incorrect response :(")
            
        
        
            
    
    
