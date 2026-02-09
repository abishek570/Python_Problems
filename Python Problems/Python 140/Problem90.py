inp = str(input("Enter the email address: "))

def get_username(inp):
    
    if inp.count("@")==1:
        for i in range(len(inp)):
            if inp[i]=="@":
                name = inp[0:i]
                return f"Username of this email-id is {name}"
    return "Please, Provide a valid email-id!"
        
print(get_username(inp))