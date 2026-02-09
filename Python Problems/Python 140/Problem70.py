## key, value list into flat dictionary

a = [("a",1),("b",2)]

dic = {}
print(type(dic))
for i,j in a:
    dic[i]=j

print(dic)
print(type(dic))