import os
print(os.getcwd())
os.chdir("D:\Programming\Python\yt\packages")
print(os.getcwd())
with open ("test.txt","w") as f:
    f.write("This is a testfile") 