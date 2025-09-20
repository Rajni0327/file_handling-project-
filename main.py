from pathlib import Path
import os 

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}") 

def createFile():
    try:
        readFileAndFolder()
        name = input("enter the file name with extension : ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                content = input("enter the content of the file : ")
                fs.write(content)
            print(f"FILE SUCCESSFULLY CREATED ")
        else:
            print("file already exists")

    except Exception as err:
        print(f"an error coccured as {err}")


def readFile():
    try:
        readFileAndFolder()
        name = input("enter the file name with extension : ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                content = fs.read()
                print(content)

                print("file successfully read")
        else:
            print("file does not exist")
    except Exception as err:
        print(f"an error coccured as {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("enter the file name with extension : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the file  ")
            print("press 2 for overwriting the data in the file  ")
            print("press 3 for appending the content in  the file  ")

            res= int(input("enter your choice : "))
            try :
                if res == 1 :
                    new_name = input("enter the new name of the file with extension : ")
                    p2 = Path(new_name)
                    p.rename(new_name)
                    print("file name successfully changed")
                elif res == 2 :
                    with open(p, 'w') as fs:
                        content = input("enter the content of the file to be updated : ")
                        fs.write(content)
                        print("file successfully updated")
                elif res == 3 :
                    with open(p, 'a') as fs:
                        content = input("enter the content of the file to be append : ")
                        fs.write(content)
                        print("file successfully appended")
                else :
                    print("invalid choice")
            except Exception as err :
                print(f"an error coccured as {err}")
            # with open(p, 'a') as fs:
            #     content = input("enter the content of the file to be updated : ")
            #     fs.write(content)
            # print("file successfully updated")
        else:
            print("file does not exist")
    except Exception as err:
        print(f"an error coccured as {err}")

def deleteFile():
    try:
        readFileAndFolder()
        name = input("enter the file name with extension that you want to delete  : ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file successfully deleted")

        else:
            print("file does not exist")
    except Exception as err:
        print(f"an error coccured as {err}")


print ("press 1 for creating a file ")
print ("press 2 for reading a file ")
print ("press 3 for updating a file ")
print ("press 4 for deleting a file ")

check = int(input("enter your choice : "))

if check == 1 :
    createFile()
elif check == 2 :
    readFile()
elif check == 3 :
    updateFile()
elif check == 4 :
    deleteFile()
else :
    print("invalid choice")