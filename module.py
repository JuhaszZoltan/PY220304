class Kategoria:
    def __init__(self, sor: str):
        v = sor.strip().split(';')
        self.nev = v[0]
        self.tulelo = int(v[1])
        self.eltunt = int(v[2])
        self.szemely = self.tulelo + self.eltunt


def beolvas(f: str, e: str):
    kategoriak = []
    for s in open(file = f, encoding = e):
        kategoriak.append(Kategoria(s))
    return kategoriak


def osszes(ks: list):
    sum = 0
    for k in ks:
        k: Kategoria
        sum += k.szemely
    return sum


def nev_keres(ks: list, t: str):
    for k in ks:
        k: Kategoria
        if t in k.nev:
            return True
    return False


def kulcsszavas_kategoriak(ks: list, t: str):
    for k in ks:
        k: Kategoria
        if t in k.nev:
            print(f'\t{k.nev} {k.szemely} fő')


def meghaladta(ks: list):
    val = []
    for k in ks:
        k: Kategoria
        if k.eltunt > k.szemely * .6:
            val.append(k)
    return val


def legtobb_tulelo(ks: list):
    maxi = 0
    for i in range(1, len(ks)):
        if ks[i].tulelo > ks[maxi].tulelo:
            maxi = i
    return ks[maxi].nev