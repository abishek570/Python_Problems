## Area of Hexagon

import math

def area_of_hexa(side):
    area = (3*math.sqrt(3)*(side**2))/2
    return round(area,1)

print(area_of_hexa(1))
print(area_of_hexa(2))
print(area_of_hexa(3))
