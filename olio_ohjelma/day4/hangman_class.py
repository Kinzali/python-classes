import random

class Hirsipuu:
    
    def __init__(self,words):
        self.words = words
        self.start_game()
    
    def start_game(self):
        
        correct=random.choice(self.words) #arpoo listasta yhden sanan

        hidden=""
        guess=""

        # for _ in correct:
        #     hidden += "_"

        hidden = "_"*len(correct) # ______

        lst = list(hidden) # ['_','_','_','_','_','_']

        while hidden != correct:
            guess = input("Anna kirjain tai sana:\n")
            if guess == correct:
                hidden = correct
            else:
                for index,char in enumerate(correct):
                    if char == guess:
                        lst[index] = char
                        hidden = ''.join(lst) #muutetaan takaisin stringiksi
                if guess not in correct:
                    print(f"kirjainta {guess} ei löytynyt")
                print(''.join(lst))

        print("CORRECT!")   
    
    @classmethod
    def from_csv(cls,filename):
        with open(filename,mode='r',encoding='utf-8')as f:
            wordlist = list(csv.reader(f))
            return cls(wordlist)
            
            # rows = []
            # for row in f.readlines[]:
            #     rivi = row.strip().split(',')
            #     rows.append(rivi)
            # print(rows)
Hirsipuu.from_csv('words.csv')