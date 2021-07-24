alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "encode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position > 25:
                new_position -= 26
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            if new_position < 0:
                new_position += 26
            cipher_text += alphabet[new_position]
        print(f"The decoded text is {cipher_text}")

# -------------------ALTERNATE------------------------------------


def caesar_two(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
            new_position -= 26
        if new_position < 0:
            new_position += 26
        end_text += alphabet[new_position]
    print(f"The {direction}'d text is {end_text}.")


caesar(text, shift, direction)
caesar_two(text, shift, direction)

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")


# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

# # TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
