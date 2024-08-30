import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

input_text = input('Enter a message to encrypt: ')
cipher = ""

for letter in input_text:
    index = chars.index(letter)
    cipher += key[index]

print(f"original message: {input_text}")
print(f"encrypted message: {cipher}")
print(50 * '*')

#DECYPTION:
cipher = input('Enter a message to encrypt: ')
input_text = ""
for letter in cipher:
    index = key.index(letter)
    input_text += chars[index]

print(f"encrypted message: {cipher}")
print(f"original message: {input_text}")
