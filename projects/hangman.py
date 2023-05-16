import random
from words import words 

#print(words)

def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words) 
    word_letters = set(word)
    alphabet = set()
    used_letters = set()  
    
    lives = 6 
    
    while len(word_letters) > 0 and lives > 0:
        #letters used 
        print('You have', lives,'lives left and you have used these letters: ',' '.join(used_letters))
        
        # what current word is (ie w - R)
        word_list =[letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list ))
        
        
        user_letter = input('Guess a letter').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(used_letters)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives -1 
                print('Letter is not in word.')
                
        elif user_letter in  used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again')  

    if lives == 0:
        print('you dies, sorry.The word was', word)
    else:          
        print('you guessed the word', word, '!!')        
hangman()   

user_input = input('Guess a letter: ')
print(user_input)
