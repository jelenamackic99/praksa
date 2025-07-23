def separate_integer(s):
    s1=set()
    s2=set()
    for item in s:
        if type(item) is int:
            s1.add(item)
        else:
            s2.add(item)
    return s1,s2

s=("RTRK", "Andjela", 1 , 2 , 3)
s1,s2=separate_integer(s)
print(s1)
print(s2)