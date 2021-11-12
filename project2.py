#Ask user for namena
name = input("enter your name:")

#Ask user for age
age = int(input("enter your age:"))
print(type(age))

#Ask user for City
city = input("enter your city:")

# Ask user what they enjoy
love = input("wat do you enjoy most:")

#Create output text
string = "your name is {} and you live in {}. your age is {} you love {} "
output = string.format(manoj, kadapa, 28, cric)
#Print output to screen
print(output)
