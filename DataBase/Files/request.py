import index
import time as t
import os
import time

print("Welcome")
print("to create a file do _new and NAME : will show up")
print("type in your file name afterwards.")
print("do _edit to edit a file, bare in mind that you have to type in the .filetype")
print("File types need to be typed in like: .json, .xml, and need to be manualy typed as you would normally")
print("it wont edit the text it would just be (again for example pourpeses): EXAMPLE TEXT")
print("_read will read files")
print("_del deletes files")

time.sleep(1.5)

while 3 > 2:
    t.sleep(1)
    inputbar = input("SETTINGS: ")
    if inputbar == "_new":
        inp = input("NAME : ")
        ftype = input("FILE TYPE : ")
        index.files.new(inp.lower() + ftype)
    if inputbar == "_edit":
        inp = input("FILE NAME : ")
        checkFile = os.path.isfile(inp)
        if checkFile == True:
            index.files.edit(inp.lower())
    if inputbar == "_read":
        inp = input("FILE NAME : ")
        checkFile = os.path.isfile(inp)
        if checkFile == True:
            index.files.read(inp.lower())
            print("")
        t.sleep(2.5)
    if inputbar == "_del":
        inp = input("FILE : ")
        os.remove(inp.lower())
    if inputbar == "_exit":
        break
