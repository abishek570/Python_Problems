# Most Frequent Element in a String based on leproxical order

import re

s = 'weuewnfwenwfeffff'
a =[]
for i in range(len(s)):
    if s.count(s[i])>1:
        a.append(s[i])
a.sort()
print(a)
b = set(a)
b = list(b)
print(b)
