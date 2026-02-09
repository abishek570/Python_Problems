## Generators

class DivisibleBySeven:
    def __init__(self,n):
        self.n = n
        n = n
    def generate_divisible_by_seven(self):
        for num in range(self.n + 1):
            if num%7 == 0:
                yield num


d = DivisibleBySeven(100)

a = d.generate_divisible_by_seven()

print(a)

for i in a:
    print(i)
    