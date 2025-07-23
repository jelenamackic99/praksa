def conver_to_ASCII(s):
    niz=[]
    for item in s:
        niz.append( ord(item) )
    return niz


s="Ivana"
print(conver_to_ASCII(s))