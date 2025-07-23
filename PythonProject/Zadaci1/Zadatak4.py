def keys_values(r):
    s1=set()
    lista=[]
    for k in r:
        s1.add(k)
        lista.append(r[k])
    return s1,lista


r = {"boja": "plava", "precnik": 3000, "Ime" : "Andjela"}
s1,lista=keys_values(r)
print(lista)
print(s1)