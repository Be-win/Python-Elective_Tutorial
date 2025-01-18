def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                shift = ord(char) + key
                if shift > ord('Z'):
                    shift = shift - ord('Z')
                    shift += ord('A') - 1
                encrypted_message += chr(shift)
            elif char.islower():
                shift = ord(char) + key
                if shift > ord('z'):
                    shift = shift - ord('z')
                    shift += ord('a') - 1
                encrypted_message += chr(shift)
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(message, key):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                shift = ord(char) - key
                if shift < ord('A'):
                    shift = ord('A') - shift
                    shift = ord('Z') - shift + 1
                decrypted_message += chr(shift)
            elif char.islower():
                shift = ord(char) - key
                if shift < ord('a'):
                    shift = ord('a') - shift
                    shift = ord('z') - shift + 1
                decrypted_message += chr(shift)
        else:
            decrypted_message += char

    return decrypted_message


input_str = input("Enter a string: ")
code = int(input("Enter the code: "))

print("Choose your option:")
print("1. Encrypt")
print("2. Decrypt")

option = int(input("Enter your option: "))

if option == 1:
    print("Encrypted Message:", encrypt(input_str, code))
elif option == 2:
    print("Decrypted Message:", decrypt(input_str, code))
else:
    print("Invalid option!")
