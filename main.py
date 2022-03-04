import module as m

# 1. feladat:
kategoriak = m.beolvas('titanic.txt', 'utf-8')

# 2. feladat:
print(f'2. feladat: {len(kategoriak)} db')

# 3. feladat:
print(f'3. feladat: {m.osszes(kategoriak)} fő')

# 4. feladat:
kulcsszo = input('4. feladat: kulcsszó: ')
van = m.nev_keres(kategoriak, kulcsszo)
if van:
    print('\tVan találat!')
    # 5. feladat:
    print('5. feladat:')
    m.kulcsszavas_kategoriak(kategoriak, kulcsszo)
else: print('\tNincs találat.')

# 6. feladat:
print('6. feladat:')
megh = m.meghaladta(kategoriak)
for k in megh:
    k: m.Kategoria
    print(f'\t{k.nev}')

# 7. feladat
print(f'7. feladat: {m.legtobb_tulelo(kategoriak)}')