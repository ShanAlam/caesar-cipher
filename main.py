from art import logo

# List of all letters in alphabet
# Pasted twice so alphabet loops back to beginning 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function used to encrypt and decrypt messages
def ceasar(text, shift, direction):
  
  # String which will hold the encrypted/decrypted message
  ceasar_text = ""

  # If the shift entered by the user is very large, 'shift' will be altered
  if shift > 26:
    shift = shift%26

  # If user chose to encrypt message...
  if direction == "encrypt":
    # For each letter in the message...
    for letter in text:
      # If it is a special charecter
      if letter not in alphabet:
        # Add to the string without altering
        ceasar_text += letter
      # Otherwise...
      else:
        # Find the position of the current letter in the alphabet
        position = alphabet.index(letter)
        # Increment the position by the shift amount to find position of new letter and add to the string
        ceasar_text += alphabet[position + shift]
    print(f"The encrypted text is {ceasar_text}")

  # If user chose to decrypt message...
  elif direction == "decrypt":
    # For each letter in the message...
    for letter in text:
      # If it is a special charecter...
      if letter not in alphabet:
        # Add to the string without altering
        ceasar_text += letter
      # Otherwise...
      else:
        # Find the position of the current letter in the alphabet
        position = alphabet.index(letter)
        #Decrement the position by the shift amount to find position of original letter and add to the string
        ceasar_text += alphabet[position - shift]
    print(f"The decrypted text is {ceasar_text}")

  # If user entered invalid input, terminate program
  else:
    print("Invalid input, program terminated")

# Printing ASCII art
print(logo)

# Main loop
termination = "no"
while termination == "no":
  
  user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  user_text = input("Type your message:\n").lower()
  user_shift = int(input("Type the shift number:\n"))

  ceasar(text=user_text, shift=user_shift, direction=user_direction)
  
  termination = input("Type 'yes' if you want the program to terminate. Otherwise type 'no':\n").lower()
  
    
    


