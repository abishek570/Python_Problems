def move_to_end(l1,element):
    if element not in l1:
        return "Please, Provide the correct element!"
    else:
        for i in range(len(l1)):
            if l1[i]==element:
                l1.pop(i)
                l1.append(element)
                return l1
    
print(move_to_end([1, 3, 2, 4, 4, 1], 1))