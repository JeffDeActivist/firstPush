print("LOG IN TO YOUR ACCOUNT")
print("Enter your details to log in")
name = str(input("Enter your name :"))
password = input("Enter your password: ")
password2 = input("Enter your password again: ")
if password == password2:
    print("Log in successfully for user", name)
elif password != password2:
    print("Wrong credentials entered.Retry")
else:
    print("Can't identify user")
