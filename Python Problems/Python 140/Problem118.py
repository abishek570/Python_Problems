## Dict calculations 

diction = [{ 'name': 'John', 'age': 21, 'budget': 23000 },
            { 'name': 'Steve', 'age': 32, 'budget': 40000 },
            { 'name': 'Martin', 'age': 16, 'budget': 2700 }]

budget = 0
for i in diction:
    for key,value in i.items():
        if key == "budget":
            budget+=value

print(budget)