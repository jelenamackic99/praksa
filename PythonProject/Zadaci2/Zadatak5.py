import sys

def findASCII(num):
    if 0 <= num <= 255:
        return chr(num)
    else:
        raise ValueError()


num=4448
try:
    b=findASCII(num)
    print(b)
except Exception as e:
    print("Desio se izuzetak")