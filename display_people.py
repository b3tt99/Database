from main import People

mypeople = People.select()
for person in mypeople:
    print(person.p_name, person.p_phone_number, person.p_email, person.p_county, person.p_gender, person.p_religion)