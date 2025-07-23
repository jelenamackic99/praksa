import os



os.environ["PASSWORD"] = "12345678aa"
user=os.environ["USERNAME"]
password=os.environ["PASSWORD"]
ime_fajla=user+".txt"

if not os.path.exists(ime_fajla):
    with open(ime_fajla, "w") as f:
        f.write(password + '\n')
else:
    with open(ime_fajla, "r") as f:
        prva_linija = f.readline().strip()
        if( prva_linija != password ):
            with open(ime_fajla, "w") as f:
                f.write(password + '\n')



