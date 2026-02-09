## Removing specific element

def remove_char(input_str,i):
    input = input_str[:i]+input_str[i+1:]
    return input

input_str = "Hello, wWorld!"
i = 7 # Index of the character to remove
# Remove the i-th character
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character : {new_str}")