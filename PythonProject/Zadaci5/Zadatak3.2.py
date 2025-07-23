
class Razlomak:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return f"{self.x}/{self.y}"

    def __mul__(self, other):
        return Razlomak(self.x*other.x, self.y*other.y)

    def __add__(self, other):
        return Razlomak(self.x*other.y+self.y*other.x, self.y*other.y)


r1=Razlomak(2,5)
r2=Razlomak(2,3)
r3=r1+r2
print(r3)
print(r1*r2)