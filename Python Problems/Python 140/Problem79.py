## Counting number of letters and numbers from a string
 
s1 = str(input("Enter the String: "))

import re

a = re.findall("[a-z,A-Z]",s1)

b = re.findall("[0-9]",s1)

print("LETTER: ",len(a))

print("NUMBERS: ",len(b))