def password_checker():
    correct_password = "batman"
    username = input("Enter your name: ")
    enter_password = input("Enter your password: ")

    while enter_password != correct_password:
        enter_password = input("Wrong Password! Enter again: ")
    
    message = "Hi %s you are logged in" % username
    print(message)
password_checker()
