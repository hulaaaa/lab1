def process(text, key, mode):
    key = key.lower()
    result = []
    i = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            shift = shift if mode == 'e' else -shift
            result.append(chr((ord(char) - base + shift) % 26 + base))
            i += 1
        else:
            result.append(char)
    return ''.join(result)

text = input("Tekst: ")
key = input("Klucz: ")
mode = input("Tryb (e=szyfruj, d=odszyfruj): ").strip().lower()

print(process(text, key, mode))
