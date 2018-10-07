def write_temperatutes(celsius, filepath):
    if celsius < -273.15:
        return "That temperature doesn't make sense"
    else:
        fahrenheit = celsius*9/5 + 32
        with open(filepath, "w") as myfile:
            myfile.write(str(fahrenheit))

enter_temp = float(input("Enter the temperature: "))

write_temperatutes(enter_temp, "temperatures.txt")