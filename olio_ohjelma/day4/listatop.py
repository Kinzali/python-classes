h# listan luonti
lista = ['a','b','c','D']

# listan pituus
print (len(lista)) #4

# listan ensimmäinen arvo
print(lista[0]) # lista.pop(0)

# listan viimeinen arvo
print(lista[-1]) # [len(lista)-1]

# listan loppuun lisääminen
lista.append('e')
print(lista)

# objektin tietotyypin selvittäminen
print(type(lista))

# tulostetaan listasta arvot b ja c indeksien mukaan
print(lista[1:3]) #indeksiä 3 ei enää huomioida

# tulostetaan 3 ensimmäistä indeksiä
print(lista[:3]) #sama kuin [0:3]

# tulostetaan indeksistä 1 eteenpäin kaikki
print(lista[1:])

# tietyn kirjaimen haku listasta
kirjain='b'
if kirjain in lista:
    print("kirjain löytyy")
    print(lista.index(kirjain)) #indexin mukaan 
else:
    print("ei löytynyt")

# listan indeksipaikan arvon muuttaminen
lista[1] = 'B'
print(lista)

# listan ison kirjaimen muuttaminen pieneksi
# käyttäen lower()-metodia
lista[1] = lista[1].lower() #löytyy myös upper()
print(lista)

# for-loopilla kaikkien listan arvojen 
# muutaminen isoiksi kirjaimiksi:
for i in lista:
#for i in range(len(lista)):
    lista[lista.index(i)] = i.upper()
    #lista[i] = lista[i].upper()

print(lista)

# isoiksi kirjaimiksi list comprehensionin 
# #avulla
lista = [i.upper() for i in lista]
print(lista)

#mappauksen avulla
lista=(list(map(str.upper,lista)))
print(lista)

#map-esimerkki 
def addition(n):
    return n + n
 
# We double all numbers using map()
numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(list(result))

# listaan lisäys tiettyyn indeksipaikkan
# esim. pieni d-kirjain ennen isoa D-kirjainta
lista.insert(3,'d')
print(lista)

# listan lisääminen listan sisään viimeiseen
# indeksipaikkaan
luvut = [1,2,3]
#lista.append(luvut)
print(lista)

# kahden listan yhdistäminen...
#lista.extend(luvut)
print(lista)

#tai
lista += luvut
print(lista)

# listan indeksipaikan arvon poisto
lista.remove('d')
print(lista)
# tai
#del lista #koko lista-objektin poisto
del lista[4] # E pois listasta
print(lista)

x = lista.pop(lista.index('D')) # tai int (indeksipaikka)
print(x)
print(lista)

# listan tyhjäys
#lista.clear()
print(hex(id(lista))) 
#lista=[] #eri muistipaikka kuin aiemmassa

#print(id(lista))
#print(lista)

# listan arvot for-loopilla samalle riville

#for kirjain in lista:
#    print(kirjain, end='') # esim. ',' csv-tekoon

# luo ylläolevasta list comprehension-versio
[print(kirjain, end='')for kirjain in lista]

hedelmat = ['banana','apple','kiwi','cherry','mango']
uusi_lista =[]

# käy läpi kaikki hedelmät, ja katso sisältääkö
# hedelmä a-kirjaimen. Mikäli sisältää, lisää
# uuteen listaan. Tulosta lopuksi uusi lista.

# for h in hedelmat:
#     #if h.count('a')>0:
#     if 'a' in h:
#         uusi_lista.append(h)

# print(uusi_lista)

#LISÄTEHTÄVÄ:
# muodosta list comprehensionilla :
# a) sama lopputulos
#uusi_lista=[h for h in hedelmat if 'a' in h]
#print(uusi_lista)
# b) uuteen listaan kaikki, paitsi apple
#uusi_lista = [h for h in hedelmat if 'a' in h and h!='apple']
uusi_lista =[h for h in hedelmat if h!= 'apple']
print(uusi_lista)

# kaikki isoiksi kirjaimiksi list comprehensionin avulla
uusi_lista = [h.upper() for h in hedelmat]
print(uusi_lista)

# muutetaan kaikki listan arvot APPLE:iksi
uusi_lista = ['APPLE' for h in hedelmat] 
print(uusi_lista)

lista=['x','X','vv','cc','caaa','a']

# lista aakkosjärjestykseen # isot kirjaimet tulevat ennen pieniä!

lista= ["5","3","1",'a']
lista.sort()
print(lista)

# lista käänteiseen aakkosjärjestykseen
x = lista.sort(reverse=True)
print(lista)

banaani = "banana"

#konvertoidaan string listaksi 
banaani = list(banaani) 
print(banaani) # ['b','a',n','a','n,'a']

 #lista->takaisin stringiksi
banaani = ''.join(banaani)
print(banaani) #banana

for index, kirjain in enumerate(banaani):
    print(index,kirjain)
    # 0 b
    # 1 a
    # 2 n
    # 3 a
    # 4 n
    # 5 a

