# listan luonti
lista = ['a','b','c','d']

# merkkijono = ""

# objekti = None 

print(len(lista))

# listan ensimmäinen arvo
print(lista[0])

# listan viimeinen arvo
print(lista[-1])  # [len[lista]-1]

# listan loppuun lisääminen
lista.append('e')
print(lista)

#objektin tietotyypin selvittäminen
print(type(lista))


#tulostetaan listasta arvot b ja c indeksien mukaan
print(lista[1:3])  # indeksiä 3 ei enää huomioida


#tulostetaan 3 ensimmäistä indeksiä
print(lista[:3]) #sama kuin[0:3]



#tulostetaan indeksisitä 1 eteenpäin kaikki
print(lista[1:])

kirjain = 'b'

if kirjain in lista:
    print("kirjain löytyy")
    print(lista.index(kirjain))
else:
    print("kirjain ei löytynyt")

#listan indeksipaikan arvon muuttaminen

lista[1] = 'B'
print(lista)

#listan ison kirjaimen muutaminen pieneksi
#käyttäen lower()- metodia

lista[1] = lista[1].lower() #löytää myös upper()
print(lista)
for i in lista:
    
#for-loopilla kaikkien listan arvojen
#muutaminen isoksi kirjaimksi:
# for i in range(len(lista)):
     lista[lista.index(i)] = i.upper()
    # lista[i] = lista[i].upper() 
    
print(lista)

# isoiksi kirjaimiksi list comprehensionin
# avulla

lista = [i.upper() for i in lista]

print(lista)

#mappauksen avulla 
lista = (list(map(str.upper,lista)))
print(lista)

#we double all the numbers using map ()
# numbers = (1,2,3,4)
# result = map(addition, numbers)
# print(list(result))

#listan tyhjäys
# lista.clear()
# print(lista)



#listan arvot for -loopilla samalle riville 

for kirjain in lista:
    print(kirjain, end= ',')
    
#luo ylläolevasta list comprehension-versio
[print(kirjain, end='')for kirjain in lista]

#harjoittelu:
hedelmat = ['banana','apple','kiwi','cherry','mango']
uusi_lista = []
#käy läpi kaikki hedelmät, ja katso sisältääko 
#hedelmä a-kirjaimen. Mikäli sisältää, lisää
#uuteen listaan. Tulosta lopuksi uusi lista.   

hedelmat = ['banana', 'apple', 'kiwi', 'cherry','mango']

for h in hedelmat:
    if h.count('a')>0:
        if 'a' in h:
            uusi_lista.append(h)
            
print(uusi_lista)


lista= ['b','x','vv','cc','caaa','a']    
#lista aakkosjärjestykseen #isot kirjaimet tulevat ennen pieniä!
lista= ["5","3","1",'a']
lista.sort()
print(lista)

#lista käänteiseen aakkosjärjestykseen
x= lista.sort(reverse=True)
print(lista)


# vastaus = "banana"
#hidden = "b_____"
# arvaus = input("syötä kirjain tai koko sana:")
# _a_a_a

banaani = "banana"
banaani = list(banaani) #konvertoidaan listaksi
print(banaani)


banaani = ''.join(banaani) # lista -> takaisin stringiksi
print(banaani)

    
for index, kirjain in enumerate(banaani):
    print(index,kirjain)


banaani = 'banana'
banaani = list(banaani)
print(banaani) #['b','a','n','a','a','n','i']

banaani = ''.join(banaani)
print(banaani) 

for index, kirjain in enumerate(banaani):
    print(index,kirjain)
    
#harjoitus

# omena = 'apple'
# omena = list(omena)
# print(omena) #['a','p','p','l','e']

# omena = ''.join(omena)
# print(omena)

# for index, kirjain in enumerate(omena):
#     print(index,kirjain)



# name = 'kinza'
# name = list(name)
# print(name) #['k','i','n','z','a']

# name = ''.join(name)
# print(name)

# for index, kirjain in enumerate(name):
#   print(index,kirjain)
  
 # correct = "banana"
#hidden = "_____"
# arvaus = input("syötä kirjain tai koko sana:")
#(käyttäjä syöttää a:n, näytetään:)
# _a_a_a
# ja kysytään taas uutta kirjainta/sanaa
#kunnes sana on "valmis"

words = ['banana','apple','kiwi','cherry','mango']
import random
correct = random.choice(words) #arpoo listasta yhden sanan

hidden = ""
guess = ""

# for _  in correct:
#     hidden += "_"
    
hidden = "_"*len(correct)

lst = list(hidden)

while hidden != correct: 
    guess = input("Anna kirjain tai sana:\n")
    if guess == correct:
        hidden = correct
    else:
        for index, char in enumerate(correct):
            if char == guess:
                lst[index] = char
                hidden = ''.join(lst)
        if guess not in correct:
            print(f"kirjainta {guess} ei löytynyt")
        print(''.join(lst))
            
print("CORRECT!")

# #harjoitus 
# muuta ohjelma niin, että pyörii hirsipuu-luokassa.

# anna luokalle lista sanoista (esim.words) parametrina
# ja aste konstruktorissa olion käyttöön

# kutsu konstruktorissa(viimeisenä)
# start_game()-metodia, ja siirrä toiminnallisus sinne.
# ----
# sanalista=['banana','apple','kiwi','cherry','mango']

# hirsipuu(sanalista)
import random
words = ['banana','apple','kiwi','cherry','mango']

class hirsipuu:
    def __init__(self,words):
        self.words = words
        
    def start_game(self):
        correct= random.choice(self.words)

        hidden = ""
        guess = ""

        # for _  in correct:
        #     hidden += "_"
    
        hidden = "_"*len(correct)

        lst = list(hidden)

        while hidden != correct: 
            guess = input("Anna kirjain tai sana:\n")
            if guess == correct:
                hidden = correct
            else:
                for index, char in enumerate(correct):
                    if char == guess:
                        lst[index] = char
                        hidden = ''.join(lst)
                if guess not in correct:
                    print(f"kirjainta {guess} ei löytynyt")
                print(''.join(lst))
                    
words = ['banana','apple','kiwi','cherry','mango']
hirsipuu(words)





    









