import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generate a random password based on user-defined criteria.
    """
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character set (letters, numbers, symbols) must be selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    passwords = set()  # To store generated passwords and ensure uniqueness

    while True:
        # Get user input for password criteria
        length = int(input("Enter the length of the password: "))
        use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        # Generate a new password
        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            # Check if the generated password is unique
            if password not in passwords:
                passwords.add(password)
                print("Generated Password:", password)
            else:
                print("Generated a duplicate password. Please try again.")

        # Ask the user if they want to generate another password
        again = input("Do you want to generate another password? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
