def decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

text = input("Szyfrogram: ")

for shift in range(1, 26):
    print(f"Klucz {shift:2d}: {decrypt(text, shift)}")
