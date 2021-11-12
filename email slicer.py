email = input("please provide ur email id:")
username = email[:email.index("@")]
domain = email[email.index("@")+1:] 
output = "your user name is: {} & your domain name is {}".format(username,domain)
print(output)
 
