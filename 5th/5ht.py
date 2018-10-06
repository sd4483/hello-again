def read_file():
    myfile = open("fruits.txt")
    content = myfile.read()
    print(content)
    content = content.splitlines()
    myfile.close()
    print(content)
read_file()


def for_loop():
    batman_movies = ['Batman Begins', 'The Dark Knight', 'The Dark Knight Rises']
    fav_movie = input("what's your fav movie?")
    if fav_movie in batman_movies:
        print("Now you are my friend. My fav movies: ")
        for movies in batman_movies:
            print (movies)
    else:
        print("Please f*off")
for_loop()

def for_loop2():
    a = [1,2,3,4,5]
    for item in a:
        if item > 2:
            print(item)
for_loop2()

def len_fruits():
    myfile = open("fruits.txt")
    content = myfile.read()
    myfile.close()
    content = content.splitlines()
    for fruits in content:
        print(len(fruits))
len_fruits()

def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

temparatures = [10, -20, 100]
for temp in temparatures:
    print(cel_to_fahr(temp))
        