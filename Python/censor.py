inputtedWord = input("Enter a word: ").lower()

vowels = set('aeiou') #using a set for faster lookups
censored_word = ''

for char in inputtedWord:
    if char in vowels:
        censored_word += '*'
    else:
        censored_word  += char

print("THE ORIGINAL TEXT: ", inputtedWord)
print("THE CENSORED TEXT: ", censored_word)


