from abc import ABC, abstractmethod

class Adder(ABC):
    @abstractmethod
    def add(self,x,y):
        pass


class ListAdder(Adder):
    def add(self,x,y):
        return x+y

class DictAdder(Adder):
    def add(self,x,y):
        return x|y


A=ListAdder()
a=[1,2,3]
b=[4,5,5]
c=A.add(a,b)
print(c)
R=DictAdder()
r1 = {"boja": "plava", "precnik": 3000, "Ime" : "Andjela"}
r2 = {"boj": "plava", "precni": 3000, "Im" : "Andjela"}
c=R.add(r1,r2)
print(c)