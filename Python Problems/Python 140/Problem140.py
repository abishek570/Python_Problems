## Replacing vowels with characters

def vow_replace(string, pat):
    a = "aeiouAEIOU"
    new_str = ""
    for i in range(len(string)):
        if string[i] in a:
            new_str+=pat
        else:
            new_str+=string[i]
    return new_str

print(vow_replace("apples and bananas", "u"))