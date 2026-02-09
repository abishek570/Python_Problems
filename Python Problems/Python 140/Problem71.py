from collections import OrderedDict

ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])

new_item = ('a',5)

ordered_dict1 = OrderedDict([new_item])

ordered_dict1.update(ordered_dict)

print(ordered_dict1)