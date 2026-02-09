def isogram(s):
    for i in s:
        if s.count(i)>1:
            return 0
    else:
        return 1
    
print(isogram("machine"))


a = [1,1,1,2,2,2,3,3]

a.remove(1)

print(a)