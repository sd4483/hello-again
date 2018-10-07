def with_context_manager():
    """
    This is a better way to create and write to a file,
        as there is no need to use the close method 
            to close the file after wrtiting it.
    """
    with open("example.txt", "w") as myfile:
        myfile.write("A good day!")
with_context_manager()