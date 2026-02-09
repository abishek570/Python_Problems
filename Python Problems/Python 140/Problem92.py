## Pronounciation helping

s = str(input("enter the hardest string: "))
def shutter(s):
    ell = "..."
    s = s.lower()
    s = s[:2]+ell+s[:2]+ell+s[:]
    return s

print(shutter(s))

