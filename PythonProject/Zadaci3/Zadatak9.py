def decor(f):
    def check(a,b):
        if (b!=0 and type(a)==int and type(b)==int):
            return f(a,b)
        else:
            print("Neispravni argumenti funkcije")
    return check
@decor
def division(a,b):
    return a/b

a=division(10,2);
print(a)