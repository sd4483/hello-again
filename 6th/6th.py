def write_file():
    numbers = [1,2,3]
    myfile = open("newfile.txt", "w")
    for num in numbers:
        myfile.write(str(num)+"\n")
    myfile.close()
write_file()


def while_loop():
    x = 0
    while x<3:
        print("Smaller")
        x = x+1
while_loop()

