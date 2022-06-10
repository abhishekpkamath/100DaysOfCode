alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(text, shift, direction):
    new_text = ""
    if direction == "decode":
        shift = -1 * shift
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position < 0:
            new_position += 26
        elif new_position > 26:
            new_position -= 26
        new_text += alphabet[new_position]
    print(f"The {direction}d text is {new_text}")

caeser(text=text, shift=shift, direction=direction)