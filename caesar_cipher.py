alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(text, shift):
    msg = list(text)
    aux = 0
    encoded_msg = []
    for i in msg:
        aux = alphabet.index(i) + shift
        if aux > 25:
            aux -= 26  # 26 is the total letters of alphabet
        aux = alphabet[aux]
        encoded_msg.append(aux)
    print("Your message is:", "".join(encoded_msg))


def decode(text, shift):
    msg = list(text)
    aux = 0
    encoded_msg = []
    for i in msg:
        aux = alphabet.index(i) - shift
        aux = alphabet[aux]
        encoded_msg.append(aux)
    print("Your message is:", "".join(encoded_msg))


while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt or type 'leave' to leave: \n")

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encode(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decode(text, shift)
    elif direction == "leave":
        break
    else:
        print("Please choose a valid option.")
