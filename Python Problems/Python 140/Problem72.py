from collections import OrderedDict
def check_order(string, reference):
# Create OrderedDicts for both strings
    string_dict = OrderedDict.fromkeys(string)
    print(string_dict)
    reference_dict = OrderedDict.fromkeys(reference)
    print(reference_dict)
# Check if the OrderedDict for the string matches the OrderedDict f
    return string_dict == reference_dict
# Input strings
input_string = "hello world"
reference_string = "helo wrd"

print(check_order(input_string,reference_string))