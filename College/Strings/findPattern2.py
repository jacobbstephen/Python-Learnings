def find_pattern(str,pattern):
    count = 0
    str_length = len(str)
    pattern_length = len(pattern)
    for i in range(str_length - pattern_length):
        if str[i: i + pattern_length] == pattern:
            count += 1
    return count


str = input("Enter the string: ")
pattern = input("Enter the pattern: ")
count = find_pattern(str,pattern)
if count> 0:
    print(count)
else:
    print("Pattern not present")