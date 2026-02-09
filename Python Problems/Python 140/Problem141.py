## Capitalize


def ascii_capitalize(string):
    result = ''
    for i in string:
        if ord(i)%2==0:
            result+=i.upper()
        else:
            result+=i.lower()
    return result

print(ascii_capitalize("to be or not to be!"))