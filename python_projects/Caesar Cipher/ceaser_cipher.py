from logo import logo_of_game
print(logo_of_game)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text , shift):
    ciphertext = "" 
    for letters in text:
        if letters not in alphabet:
            ciphertext += letters 
            print("ERROR")
        else:
            letters in alphabet
            position = alphabet.index(letters)
            new_position = (position + shift) % len(alphabet)
            ciphertext += alphabet[new_position]
    print(f"The encoded text is: {ciphertext}")

def decrypt(ciphertext , shift):
    original_text = ""
    for letters in ciphertext:
        if letters not in alphabet:
            original_text += letters 
            print("ERROR")
        else:
            letters in alphabet
            position = alphabet.index(letters)
            neW_position = (position-shift)%len(alphabet)
            original_text += alphabet[neW_position]
                
    print(f"The decoded text is: {original_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid input! Please type 'encode' to encrypt or 'decode' to decrypt.")
        continue
    
    while True:
        text = input("Type your message: \n").lower()
        if all(char in alphabet + [' '] for char in text):
            break
        else:
            print("Invalid characters! Please use only alphabetic characters and spaces.")        

    while True:
        try:
            shift = int(input("Type the shift number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number for the shift.")

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    
    
    choice = input("Do you want to continue? Yes or No: ").lower()
    if choice not in ['yes', 'no']:
        print("Invalid input! Please type 'Yes' to continue or 'No' to exit.")
        continue
    if choice == 'no':
        break  






       



