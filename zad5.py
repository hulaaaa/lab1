import random

text = input("Wiadomosc: ")

key = [random.randint(0, 255) for _ in range(len(text))]
cipher = [ord(text[i]) ^ key[i] for i in range(len(text))]
decrypted = ''.join(chr(cipher[i] ^ key[i]) for i in range(len(cipher)))

print(f"Klucz:        {key}")
print(f"Szyfrogram:   {cipher}")
print(f"Odszyfrowany: {decrypted}")
