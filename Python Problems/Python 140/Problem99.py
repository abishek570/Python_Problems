## Vowels Replacer

def vowels_replace(s1, pat):
    a = ['a','e','i','o','u']
    new_str = ""
    for i in range(len(s1)):
        if s1[i] in a:
            new_str+=pat
        else:
            new_str+=s1[i]


    return new_str

print(vowels_replace("the aardvark", "#"))

## PROBLEM 100 

def fact(number):
    if number == 0:
        return 1
    else:
        return number*fact(number-1)
    
print(fact(10))