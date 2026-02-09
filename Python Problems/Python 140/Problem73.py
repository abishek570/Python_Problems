sample_dict = {'date': 4, 'apple': 3, 'banana': 1, 'cherry': 2}

a = sorted(sample_dict.items())

print(dict(a))

for key,value in a:
    print(f"{key}: {value}")

