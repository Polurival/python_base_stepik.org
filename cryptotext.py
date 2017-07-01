from simplecrypt import decrypt, DecryptionException

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

with open("passwords.txt", "r") as inf:
    for password in inf:
        print(password.strip())
        try:
            text = decrypt(password.strip(), encrypted).decode('utf-8')
            print(text)
        except DecryptionException:
            pass