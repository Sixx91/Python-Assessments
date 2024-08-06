import getpass
import os

# Global variable
credentials_file = "credentials.txt"

# Function to create an encryption key
def create_encryption_key():
    key_name = input("\nEnter a name for the encryption key: ")
    print(f"Encryption key '{key_name}' created.\n")

# Function to encrypt text
def encrypt_text(clear_text, shift=3):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    return "".join([char_set[(char_set.find(c) + shift) % len(char_set)] for c in clear_text])

# Function to decrypt text
def decrypt_text(enc_text, shift=3):
    char_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
    return "".join([char_set[(char_set.find(c) - shift) % len(char_set)] for c in enc_text])

# Function to view stored credentials
def view_credentials(file_path):
    if not os.path.exists(file_path):
        print("\nNo credentials found.\n")
        create_new = input("Would you like to create a new credential? (y/n): ").lower()
        if create_new == 'y':
            create_credentials(file_path)
        return
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if not lines:
            print("\nNo credentials found.\n")
            create_new = input("Would you like to create a new credential? (y/n): ").lower()
            if create_new == 'y':
                create_credentials(file_path)
            return

        print("\nStored Credentials:")
        for line in lines:
            site, enc_pwd = line.strip().split(',')
            print(f"Site: {site}, Password: {decrypt_text(enc_pwd)}")
        print()

# Function to create new credentials
def create_credentials(file_path):
    site = input("\nEnter the website name: ")
    password = getpass.getpass("Enter the password: ")
    enc_password = encrypt_text(password)
    
    with open(file_path, 'a') as file:
        file.write(f"{site},{enc_password}\n")
    
    print(f"Credentials for '{site}' stored.\n")

# Main program
def main():
    print("=======================")
    print("Apps2U Password Manager")
    print("=======================\n")
    
    choice = ''
    
    while choice != 'q':
        # Display menu
        print("\n[1] Enter 1 to create an encryption key.")
        print("[2] Enter 2 to view stored credentials")
        print("[3] Enter 3 to create new credentials")
        print("[q] Enter q to quit.")
        
        # Get user choice
        choice = input("\nMake your choice: ")
        
        # Respond to user choice
        if choice == '1':
            create_encryption_key()
        elif choice == '2':
            view_credentials(credentials_file)
        elif choice == '3':
            create_credentials(credentials_file)
        elif choice == 'q':
            print("\nExiting the menu\n")
        else:
            print("\nInvalid option, please try again.\n")
    
    print("Program exit.")

if __name__ == "__main__":
    main()
