str = "Jacob B Stephen"
vowels = ['a','e', 'i','o','u']
f = open("orginal.txt","w")
f.write(str)
f.close()

f = open("orginal.txt","r")
read_str = (f.read()).split()
dup = open("duplicate.txt","w")

for item in read_str:
    for char in item:
        if char not in vowels:
            dup.write(char + "")
f.close()
dup.close()