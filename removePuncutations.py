puncutations = """
            !()[]<>.,?/;:'"{}-_~`@#$%^&*+*|\
            """
my_str = input("Enter the string: ")

modified_str = ""
for char in my_str:
    if char not in puncutations:
        modified_str = modified_str + char
        
print(modified_str)