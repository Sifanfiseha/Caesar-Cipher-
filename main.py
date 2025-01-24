alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_or_decode):
    new_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter.isalpha():
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            new_text += alphabet[shifted_position]
        else:
            new_text += letter
    print(f"Here is the {encode_or_decode}d result : '{new_text}'")
run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
    if choice == 'no':
      run = False
      print("Goodbye.")
