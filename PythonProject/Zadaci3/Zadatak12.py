def najblizi_deljiv_sa_7():
    najblizi = None
    while True:
        broj = (yield najblizi)
        if broj % 7 == 0:
            najblizi=broj
        elif broj % 7 < 4:
            najblizi=broj-broj%7
        else:
            najblizi=broj+7-broj%7

# def generator(x,y):
#     for i in range(x,y+1):

k=najblizi_deljiv_sa_7()
print(next(k))

for i in range(1,25):
    print(k.send(i))