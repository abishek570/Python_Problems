def mapping(l):
    result = {}
    for key in l:
        result[key] = key.upper()
    return result

print(mapping(["a", "b", "c"]))