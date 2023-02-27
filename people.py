from main import People

try:
    name = input("Enter your name\n")
    phone_number = input("Enter your phone number\n")
    email = input("Enter your email\n")
    county = input("Enter your county\n")
    gender = input("Specify your gender\n")
    religion = input("Specify your religion\n")
    password = input("Enter your password\n")

    People.create(p_name=name, p_phone_number=phone_number, p_email=email, p_county=county, p_gender=gender, p_religion=religion, p_password=password)
    print("Person Created Successfully")

except:
        print("Failed to create person .Use a different email.")