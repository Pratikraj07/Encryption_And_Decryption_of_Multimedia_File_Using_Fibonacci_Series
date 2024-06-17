import os
import math

# defining the function for encryption


def file_encryption(file_name):
    # opening the file in read mode
    with open(file_name, 'r') as file:
        # reading the file
        message = file.read()
        # closing the file
        file.close()

    # initializing a blank string
    encrypted_message = ""

    # looping through each character of the message
    for character in message:
        # calculating the ASCII code of the character
        ascii_value = ord(character)
        # calculating the Fibonacci number corresponding
        # to the ASCII value
        fibonacci_value = int(
            round(((math.sqrt(5) + 1) / 2) ** ascii_value / math.sqrt(5)))
        # appending the Fibonacci number to the encrypted message
        encrypted_message = encrypted_message + str(fibonacci_value)
        encrypted_message += " "

    # writing the encrypted message to the output file
    with open("encrypted_" + file_name, 'w') as file:
        # writing the encrypted message to the file
        file.write(encrypted_message)
        # closing the output file
        file.close()

    return

# defining the function for decryption


def file_decryption(file_name):
    # opening the file in read mode
    with open(file_name, 'r') as file:
        # reading the file
        message = file.read().split()
        # closing the file
        file.close()

    # initializing a blank string
    decrypted_message = ""

    # looping through each number of the message
    for number in message:
        if not number.isnumeric():
            continue

        # calculating the ASCII value corresponding
        # to the Fibonacci number
        ascii_value = int(
            round(math.log((int(number) * math.sqrt(5)) + 0.5, ((math.sqrt(5) + 1) / 2))))
        # appending the character to the decrypted message
        decrypted_message = decrypted_message + chr(ascii_value)

    # writing the decrypted message to the output file
    with open("decrypted_" + file_name.split("_")[1], 'w') as file:
        # writing the decrypted message to the file
        file.write(decrypted_message)
        # closing the output file
        file.close()

    return decrypted_message

# main function


def main():
    # taking the file name as input from the user
    file_name = input("Enter the file name : ")
    # validating the file name
    if os.path.exists(file_name):
        # calling the encryption function
        file_encryption(file_name)
        # calling the decryption function
        decrypted_message = file_decryption("encrypted_" + file_name)
        # printing the success message
        print("File Encrypted and Decrypted Successfully.")
        # Asking for the encrypted message to decrypt
        encrypted_text = input("Enter the encrypted message to decrypt: ")
        # Decrypting the encrypted message
        decrypted_text = ""
        for number in encrypted_text.split():
            if not number.isnumeric():
                continue
            ascii_value = int(
                round(math.log((int(number) * math.sqrt(5)) + 0.5, ((math.sqrt(5) + 1) / 2))))
            decrypted_text += chr(ascii_value)
        # Printing the decrypted message
        print("Decrypted Message: ", decrypted_text)
    else:
        # printing the error message
        print("File Not Found.")
    return


# calling the main function
if __name__ == '__main_dsgsga_':
    main()

# defining the function for encryption


def file_encryption(file_name):
    # opening the file in read mode
    with open(file_name, 'r') as file:
        # reading the file
        message = file.read()
        # closing the file
        file.close()

    # initializing a blank string
    encrypted_message = ""

    # looping through each character of the message
    for character in message:
        # calculating the ASCII code of the character
        ascii_value = ord(character)
        # calculating the Fibonacci number corresponding
        # to the ASCII value
        fibonacci_value = int(
            round(((math.sqrt(5) + 1) / 2) ** ascii_value / math.sqrt(5)))
        # appending the Fibonacci number to the encrypted message
        encrypted_message = encrypted_message + str(fibonacci_value)
        encrypted_message += " "

    # writing the encrypted message to the output file
    with open("encrypted_" + file_name, 'w') as file:
        # writing the encrypted message to the file
        file.write(encrypted_message)
        # closing the output file
        file.close()

    return

# defining the function for decryption


def file_decryption(file_name):
    # opening the file in read mode
    with open(file_name, 'r') as file:
        # reading the file
        message = file.read().split()
        # closing the file
        file.close()

    # initializing a blank string
    decrypted_message = ""

    # looping through each number of the message
    for number in message:
        if not number.isnumeric():
            continue

        # calculating the ASCII value corresponding
        # to the Fibonacci number
        ascii_value = int(
            round(math.log((int(number) * math.sqrt(5)) + 0.5, ((math.sqrt(5) + 1) / 2))))
        # appending the character to the decrypted message
        decrypted_message = decrypted_message + chr(ascii_value)

    # writing the decrypted message to the output file
    with open("decrypted_" + file_name.split("_")[1], 'w') as file:
        # writing the decrypted message to the file
        file.write(decrypted_message)
        # closing the output file
        file.close()

    return decrypted_message

# main function


def main():
    # taking the file name as input from the user
    file_name = input("Enter the file name : ")
    # validating the file name
    if os.path.exists(file_name):
        # calling the encryption function
        file_encryption(file_name)
        # calling the decryption function
        decrypted_message = file_decryption("encrypted_" + file_name)
        # printing the success message
        print("File Encrypted and Decrypted Successfully.")
        # Asking for the encrypted message to decrypt
        encrypted_text = input("Enter the encrypted message to decrypt: ")
        # Decrypting the encrypted message
        decrypted_text = ""
        for number in encrypted_text.split():
            if not number.isnumeric():
                continue
            ascii_value = int(
                round(math.log((int(number) * math.sqrt(5)) + 0.5, ((math.sqrt(5) + 1) / 2))))
            decrypted_text += chr(ascii_value)
        # Printing the decrypted message
        print("Decrypted Message: ", decrypted_text)
    else:
        # printing the error message
        print("File Not Found.")
    return


# calling the main function
if __name__ == '__main__':
    main()
