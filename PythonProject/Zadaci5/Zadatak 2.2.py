from abc import ABC, abstractmethod
import os
class Uredjaj(ABC):
    svi_uredjaji=[]

    def __init__(self, serial_num, id_cloud):
        if serial_num not in Uredjaj.svi_uredjaji:
            self.serial_num = serial_num
            self.id_cloud = id_cloud
            Uredjaj.svi_uredjaji.append(serial_num)
        else:
            print("Uredjaj vec postoji!")

    @abstractmethod
    def str(self):
        pass

    def upis_u_fajl(self):
        fajl_putanja = os.environ.get('file_path')
        with open(fajl_putanja, 'a', encoding='utf-8') as f:
            f.write( "Serijski broj:" + str(self.serial_num) + "Id_cloud:" + str(self.id_cloud) + '\n' )

    @staticmethod
    def citaj_uredjaje():
        fajl_putanja = os.environ.get('file_path')
        with(open(fajl_putanja, 'r', encoding='utf-8')) as f:
            return f.readlines()


class IOt_Uredjaj(Uredjaj):
    def str(self):
        print("%d je serijski broj, a %d je id_cloud " % (self.serial_num, self.id_cloud))



def decor(f):
    def check(num):
        if num not in Uredjaj.svi_uredjaji:
            print("Uredjaj ne postoji")
        elif  Uredjaj.svi_uredjaji.count(num)>1:
            print("Uredjaj nije jedinstven")
        else:
            print("Uredjaj postoji i jedinstven je")
    return check

@decor
def provjera(num):
    pass

os.environ['file_path']='../student.txt'

i=IOt_Uredjaj(serial_num=1234,id_cloud=1234)
i2=IOt_Uredjaj(serial_num=1233,id_cloud=1233)
i.str()
i.upis_u_fajl()
i2.upis_u_fajl()
a=Uredjaj.citaj_uredjaje()
provjera(1234)
print(a)



