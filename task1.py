def caesar_cipher(text, shift, mode):
    """Encrypt or decrypt text using the Caesar Cipher algorithm."""
    result = ""
    shift = shift % 26  # Normalize shift value to range 0–25

    for char in text:
        # Encrypt only ASCII letters (A-Z, a-z)
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            shift_base = 65 if char.isupper() else 97
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces, punctuation, and numbers unchanged
    return result


def get_valid_shift():
    """Prompt until the user enters a valid integer shift."""
    while True:
        try:
            shift = int(input("Enter shift value: "))
            return shift
        except ValueError:
            print(" Invalid input... Please enter an integer number.\n")


def main():
    print("* * * * * * * Caesar Cipher Encryption or Decryption Tool * * * * * * ")

    while True:
        message = input("\nEnter your message: ")
        shift = get_valid_shift()

        # Mode selection
        print("\nChoose mode:")
        print("1. Encrypt ")
        print("2. Decrypt ")
        mode_input = input("Enter choice: ").strip().lower()

        if mode_input in ['1', 'encrypt', 'e']:
            result = caesar_cipher(message, shift, 'encrypt')
            print("\n Encrypted Message:", result)

        elif mode_input in ['2', 'decrypt', 'd']:
            result = caesar_cipher(message, shift, 'decrypt')
            print("\n Decrypted Message:", result)

        else:
            print(" Invalid choice! Please enter 1/2 or encrypt/decrypt.")
            continue

        # Ask to continue or exit
        again = input("\nDo you want to continue? (y/n): ").strip().lower()
        if again != 'y':
            print("\n- - - - - - - Exiting Caesar Cipher Program - - - - - - - ")
            break


if __name__ == "__main__":
    main()



