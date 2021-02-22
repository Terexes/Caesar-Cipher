alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_direction):
    text = input("Insert your message: \n").lower()
    shift = int(input("Insert the shift number: \n"))
    if shift > len(alphabet):
        shift = shift % 26
        print(
            f"Your shift number chosen was too high !\nYour new shift number is: {shift}")
    encoded_msg = ""
    if text_direction == "decode":
        shift *= - 1
    for char in text:
        if char in alphabet:  # checks for letters in alphabet
            position = alphabet.index(char)
            new_position = position + shift

            if new_position > 25:
                new_position -= 26
            encoded_msg += alphabet[new_position]
        else:  # if its not a letter, pass it directly to encoded_msg
            encoded_msg += char

    print(f"Your {text_direction}d message is: {encoded_msg}")


while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt or type 'leave' to leave: \n")
    if direction == "leave":
        break
    caesar(direction)
