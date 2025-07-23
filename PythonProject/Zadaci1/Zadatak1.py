from importlib.resources.readers import remove_duplicates
b=[]
def remove_duplicates (lista):
    for item in lista:
        if item not in b:
            b.append(item)
    return b

a=[1,2,3,"Python", "RTRK", "RTRK", 1, 2]
a=remove_duplicates(a)
print(a)




