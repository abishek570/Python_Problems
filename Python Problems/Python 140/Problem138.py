## Dictionary to List

def dict_to_list(diction):
    l = list(sorted(diction.items()))
    return l

print(dict_to_list({
"D": 1, 
"B": 2, 
"C": 3
 }))