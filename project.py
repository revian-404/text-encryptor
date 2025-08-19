import string 
alphabet = string.ascii_lowercase
alphabet2 = string.ascii_uppercase
user_word = input("Please enter a word : ")
user_key = int(input("Please enter a shift number : "))

def cryptography(word, key) :
    encrypted = ''
    for letter in word :
        if letter not in alphabet and letter not in alphabet2 :
            encrypted += letter
            continue
        if letter in alphabet :
            original_index = alphabet.index(letter)
            new_index = (original_index + key) % 26
            encrypted += alphabet[new_index]

        else :
            original_index = alphabet2.index(letter)
            new_index = (original_index + key) % 26
            encrypted += alphabet2[new_index]
    return encrypted

final_word = cryptography(user_word, user_key)
print(f"This is the encrypted word : {final_word}")
