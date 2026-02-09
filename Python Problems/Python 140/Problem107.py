## String Doubler

s = str(input("Enter the String: "))

new_str = ""
for i in range(len(s)):
    new_str+=2*s[i]

print(new_str)