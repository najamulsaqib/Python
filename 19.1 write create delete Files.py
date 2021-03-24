import os # importing os to delete files


f = open("demofile.txt", "a") # with a it will append content
f.write("Now the file has more content!\n")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
# print(f.read(5)) # it will read 5 characters only
# print(f.readline()) # it will read first line 
# print(f.readlines()) # it return list of lines by passing argument it will return data on particular index of list
f.close()

f = open("demofile2.txt", 'w')
f.write("Privious data will be removed")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()

if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
    os.remove("demofile.txt")
    print("File deleted sucessfully.")
else:
    print("File not found")


# os.rmdir("myfolder") # to delete folder
# You can only remove empty folders.