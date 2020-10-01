def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

current_year = int(input("whats the current year? "))
birth_year = int(input("when were you born "))
my_age = calculate_age(current_year, birth_year)
print("you are " + str(my_age))