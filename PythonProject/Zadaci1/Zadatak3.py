def reverse_value_keys(r):
    r1 = {}
    for k in r:
        pom = r[k]
        r1[pom] = k
    return r1





r = {"boja": "plava", "precnik": 3000, "Ime" : "Andjela"}
r=reverse_value_keys(r)
print(r)