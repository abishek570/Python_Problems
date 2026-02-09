def cook(balance_maavu):
    if balance_maavu == 1:
        return 1
    else:
        total = 1+cook(balance_maavu-1)
        return total
    
print(cook(3))

def add_using_recursion(number):
    if number == 0:
        return 0
    else:
        total = number + add_using_recursion(number-1)
        return total
    
print(add_using_recursion(5))

def fibonacci_recursion(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)
    
print(fibonacci_recursion(6))