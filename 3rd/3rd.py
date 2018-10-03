num = int(input("Enter a number: "))
"""input fucntion always produces a string output, so we need to convert it to integer before executing it"""

def powerof2():
    output = num**2
    return output

print(powerof2())


some_dict = {"sudheer":1234, "swathi": 3434, "rajani":4483, "purna":1111}
new_num = int(input("Enter a number: "))

def num_check():
    if new_num > 1000:
        if new_num in some_dict.values():
            print ("You're in")
        else:
            print ("Get out Mf*cker")
    else:
        print("You entered a wrong num")
num_check()
