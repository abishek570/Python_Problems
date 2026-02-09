## Binary string

def deci_to_binary(decimal):
    bin_str = ""
    while decimal>0:
        rem = decimal%2
        bin_str=str(rem)+bin_str
        decimal//=2
    return bin_str

print(deci_to_binary(14))
