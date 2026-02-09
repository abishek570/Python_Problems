def is_triplet(a,b,c):
    if (a**2)+(b**2) == c**2 or (c**2)+(b**2)==a**2 or (a**2)+(c**2)==b**2:
        return True
    else:
        return False
    
print(is_triplet(1, 2, 3))