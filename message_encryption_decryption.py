# import random
# import string
# random_char = random.choice(string.ascii_letters)
# print(random_char)
# random_alphabets = "".join(random.choices(string.ascii_letters, k = 4))
# print(random_alphabets)


import random
import string as str
import time

while True:
    try:
        user_input = int(input("1. for code, 2. for decode 3. for exit"))
        newString = [] # empty list

        # checking user choice

        if user_input == 1:
            code = ""
            string = input("Enter string for code: ")
            r1 = "".join(random.choices(str.ascii_lowercase, k = 3))
            r2 = "".join(random.choices(str.ascii_lowercase, k = 3))
            formatted_string = string.split(" ")
            for i in formatted_string:
                if len(i) >= 3: 
                    # if len(i) > 3 chars then adding r1 and string without first element 
                    # move first index to last and add r2 at end
                     
                    code = r1 + i[1:] + i[0] + r2
                    newString.append(code)
                else: # for len(i) < 3
                    code = i[::-1]
                    newString.append(code)
            print(f"YOUR CODE: {" ".join(newString)}")
        
        
        elif user_input == 2:
            string = input("Enter the string for decode: ")
            code  = ""
            formatted_string = string.split(" ")
            for i in formatted_string: # same as if block
                if len(i) >= 3:
                    code = i[3:-3]
                    code = code[-1] + code[:-1] 
                    newString.append(code)
                else:
                    newString.append(i[::-1])
            print(f"String is: {" ".join(newString)}")
        
        
        else:
             break
    
    
    except:
        print("Please enter a number 1 or 2") # end