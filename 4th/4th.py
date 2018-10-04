birth_year = int(input("Enter your birth year: "))
def calc_age(year):
    age = 2018 - year
    return age

print(calc_age(birth_year)) 

def converter(kilograms, coefficient=2.20462):
    return kilograms*coefficient

print(converter(10))

def weather_fun(celsius):
    fahrenhiet = celsius*(9/5) + 32
    return fahrenhiet

print(weather_fun(celsius = float(input("Enter the temperature: "))))

def string_length(mystring):
    if type(mystring) != str:
        return "Sorry integers don't have length"
    else:
        return len(mystring)
print(string_length("some"))