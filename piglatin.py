# ask sentence from user
original = input("hey!! write a sentence :").lower().strip()
# split the sentence into words
words = original.split()
pigword = []
#loop through words and convert into pig latin
for word in words:
#if starts with vowel, just add yay
    if word[0] in "aeiou":
        latin = "{}{}".format(word,"Yay")
        pigword.append(latin)  
        
# if starts with consonent, move con cluster to end and add ay
    else :
        index = 0
        for i in word:
            if i not in "aeiou":
                index = index + 1
            else:
                break
        latin = word[index:]+word[:index] + "ay"
        pigword.append(latin)
#stick words back together
output = " ".join(pigword)
#output final string
print(output)
