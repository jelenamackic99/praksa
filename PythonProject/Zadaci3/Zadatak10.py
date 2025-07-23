def izracunaj_povrsinu(oblik):
    def povrsina(*args):
        if oblik=="krug":
            return args[0]*args[0]*3.14
        elif oblik=="kvadrat" :
            return args[0]*args[0]
        elif oblik=="pravougaonik":
            return args[0]*args[1]
    return povrsina

kr=izracunaj_povrsinu("krug")
print(kr(2))
print(kr(4))
kv=izracunaj_povrsinu("kvadrat")
print(kv(2))
p=izracunaj_povrsinu("pravougaonik")
print(p(2,3))

