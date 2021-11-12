print("Hi dude we need below details..please provide")
name = input("What is ur name?: ")
age = input("what is ur age?: ")
print(type(age))
city = input ("where do you live?: ")
text = "Hi {}, you are {} years old and you live in {} city"
output = text.format(name,age,city)
print(output)
