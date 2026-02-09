n = int(input("Input number:"))

def convertFive(n):
        # Code here
        n = str(n)
        import re
        a = re.findall('[0-9]',n)
        for i in range(len(a)):
            if a[i]=='0':
                a[i]='5'
            else:
                pass
        a = ''.join(a)
        return int(a)
print(convertFive(n))