def encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Tekst: ")
shift = int(input("Przesunięcie (1-25): "))

enc = encrypt(text, shift)
dec = decrypt(enc, shift)

print(f"Szyfrogram:   {enc}")
print(f"Odszyfrowany: {dec}")
