import re

# Single match search
pattern1 = "is"
text1 = """My name is Harry. I am from Pakistan.
Cyclone has a Dyclone and which is Zyclone. also in earth."""
match = re.search(pattern1, text1) # used only for one match
print("Single Match:")
print(match)
print()

# Finding multiple matches
pattern2 = r"[A-Z]+yclone"
text2 = """Hey I am new to Cyclone. This is Dyclone text."""
matches = re.finditer(pattern2, text2)
print("Multiple Matches:")
for match in matches:
    print(match)
    
    # You can also print the matched text like this
    # print(text2[match.span()[0]:match.span()[1]])
