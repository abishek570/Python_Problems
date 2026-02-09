
def society_name(names):
    new_str = ""
    for i in names:
        new_str+=i[0]
    print("".join(sorted(new_str)))
society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])