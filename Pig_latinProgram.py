def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        pig_word = word+ 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

word = input("Enter the word: ")
res =pig_latin(word)
print(f'Pig Latin format for {word} is {res}')
