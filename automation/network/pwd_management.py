import random
import string

#TO-DO: Add SSL to encrypt password file

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def save_password(username, password):
    """Save the generated password to a file."""
    with open('passwords.txt', 'a') as f:
        f.write(f'{username}: {password}\n')
    print(f'Password for {username} saved successfully.')


def main():
    username = input('Enter username: ')
    password = generate_password()
    save_password(username, password)

if __name__ == "__main__":main()
