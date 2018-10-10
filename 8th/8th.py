from datetime import datetime
def merge_text_files():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as newfile:    
        for f in files:
            with open(f, "r") as myfile:
                content = myfile.read() 
                newfile.write(content + "\n")
merge_text_files()