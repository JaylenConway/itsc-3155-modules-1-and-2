#Members: Manav M., Michael, Dylan D.
words = []

for i in range(5):
    word = input('Enter a word: ')
    words.append(word)

result = ' '.join(words)

print('Words: ' + str(words))
print('One string: ' + result)