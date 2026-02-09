## PASSWORD VERIFIER

s = map(str, input("Enter the password: ").split(","))

import re

b = []
for i in s:
    if len(i)>=6 and len(i)<=12:
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])",i):
            a = True
        else:
            a = False

        if a == True:
            b.append(i)

# Returning the valid passwords
print(",".join(b))
