## Evenly divisible

def even_divisible(a,b,c) -> int:
    sums = 0
    for i in range(a,b+1,c):
        if i%c==0:
            sums+=i
    return sums

print(even_divisible(0,10,20))


## Eval function

def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return False
    
print(correct_signs("3 < 7 < 11"))