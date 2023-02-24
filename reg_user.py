from main import User

try:
    user_name = input("Enter your name \n")
    user_email = input("Enter your Email \n")
    user_password = input("Enter your Password \n")

    User.create(name=user_name, email=user_email, password=user_password)
    print("User Created Successfully")

except:
    print("Failed to create a user.Use a different email.")
