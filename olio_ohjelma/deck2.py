
#Luo tai muokkaa ohjelmaa niin, Että on 2 luokkaa: Deck ja card.
#katso card-luokasta mallia edeltävästä deck-harjoituksesta.
#muuta koodia niin, että deck-luokaan konstruktorissa tehdään Tk-luokasta olio
#ja kutsutaan:
# self.fill_deck()
# self.deal()
# self.win.mainloop()

#deal-metodissa, lisää buttonit (kortit)gridiin.
#card_luokaan konstruktorissa, hae korttien kuvat,
#muutaa photomageksi ja suurenna kuvat
#ja luo kyseisestä kortista button, joka saa kuvakseen kyseisen korttikuvan.
#buttonia painettassa tulee kutsua card-luokan change-card-metodia,
#joka muuttaa kortiin kuvan joksikin toiseksi

#e.g:
lista=['a','b','c','d','e']
for item in lista:
    if item=='b':
        lista.remove(item)
print(lista)
