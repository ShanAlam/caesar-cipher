from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text, shift, direction):
  
  ceasar_text = ""
  
  if shift > 26:
    shift = shift%26
    
  if direction == "encrypt":
    for letter in text:
      if letter not in alphabet:
        ceasar_text += letter
      else:
        position = alphabet.index(letter)
        ceasar_text += alphabet[position + shift]
    print(f"The encrypted text is {ceasar_text}")

  elif direction == "decrypt":
    for letter in text:
      if letter not in alphabet:
        ceasar_text += letter
      else:
        position = alphabet.index(letter)
        ceasar_text += alphabet[position - shift]
    print(f"The decrypted text is {ceasar_text}")

  else:
    print("Invalid input, program terminated")


print(logo)

termination = "no"

while termination == "no":
  
  user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  user_text = input("Type your message:\n").lower()
  user_shift = int(input("Type the shift number:\n"))

  ceasar(text=user_text, shift=user_shift, direction=user_direction)
  
  termination = input("Type 'yes' if you want the program to terminate. Otherwise type 'no':\n").lower()
  
    
    


