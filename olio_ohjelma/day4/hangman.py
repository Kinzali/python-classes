correct="banana"
hidden=""
guess=""

# for _ in correct:
#     hidden += "_"

hidden = "_"*len(correct)

lst = list(hidden) # ['_','_','_','_','_','_']

while hidden != correct:
    guess = input("Anna kirjain tai sana:\n")
    if guess == correct:
        hidden = correct
    else:
        for index,char in enumerate(correct):
            if char == guess:
                lst[index] = char
                hidden = ''.join(lst)
        if guess not in correct:
            print(f"kirjainta {guess} ei löytynyt")
        print(''.join(lst))

print("CORRECT!")   



