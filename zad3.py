from collections import Counter

text = input("Szyfrogram: ")

freq = Counter(c.lower() for c in text if c.isalpha())

for letter, count in freq.most_common():
    print(f"'{letter}': {count}")
