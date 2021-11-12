vowels = 0
consonents = 0
for letter in "jnjnjn134":
     if letter.lower() in "aeiou":
         vowels = vowels + 1
     else:
        if letter.lower().isalpha():
          consonents = consonents + 1
        else:
            pass
print("number of vowels = {}".format(vowels))
print("number of consonents = {}".format(consonents))
        
