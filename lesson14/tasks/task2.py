def alphabet_generator():
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        yield letter


alphabet = alphabet_generator()
for letter in alphabet:
    print(letter)
print(next(alphabet))
