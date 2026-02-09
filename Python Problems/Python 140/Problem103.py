## Reverse and Swap Case

def rev_swap(s1):
    s1 = s1[-1::-1].swapcase()
    return s1

print(rev_swap("Abhi RoshIKA"))