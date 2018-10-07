def multiple_loop_sequence():
    x = ['a', 'b', 'c']
    y = [1, 2, 3]
    for i,j in zip(x,y):
        print("{0} is {1}" .format(i,j))
multiple_loop_sequence()