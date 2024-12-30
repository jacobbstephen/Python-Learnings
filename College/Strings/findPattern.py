def find_pattern(str,pattern):
    count = 0
    index = 0
    index = str.find(pattern,index,len(str))
    while(index != -1):
        count += 1
        index = str.find(pattern,index + 1,len(str))
    return count


str = input("Enter the string: ")
pattern = input("Enter the pattern: ")
count = find_pattern(str,pattern)
if count> 0:
    print(count)
else:
    print("Pattern not present")