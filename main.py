import secrets
import string
from wonderwords import RandomWord

def calculate_password(length, type):
    characters = ''
    if type == 1:
        characters = string.ascii_letters + string.digits + string.punctuation
    elif type == 2:
        characters = string.ascii_letters + string.digits
    elif type == 3:
        characters = string.ascii_letters + string.punctuation
    elif type == 4:
        characters = string.ascii_letters
    elif type == 5:
        r = RandomWord()
        while True:
            phrase = ("-".join([r.word() for _ in range(length)]))
            if len(phrase) >= length:
                print(f"\nYour password is {phrase}")
                break
    elif type == 6:
        characters = string.digits
    if type != 5:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        print(f"\nYour password is: {password}")


def disclaimer():
    print("*** Respond with a number ***")


print("Welcome to Password Generator\n")

print("Choose a password type:")
print("1) Random")
print("2) Memorable")
print("3) Pin Number")
disclaimer()

password_type = int(input().strip())
print()

if password_type == 1:
    print("With alphabets included would you like:\n1) Numbers and Symbols\n2) Numbers Only\n3) Symbols Only\n4) Alphabet Only")
    disclaimer()
    char_type = int(input())
    print()
    print("Give a password length")
    disclaimer()
    length = int(input())
    calculate_password(length, char_type)

elif password_type == 2:
    print("Give a word length")
    disclaimer()
    length = int(input())
    calculate_password(length, 5)

elif password_type == 3:
    print("Give a password length")
    disclaimer()
    length = int(input())
    calculate_password(length, 6)