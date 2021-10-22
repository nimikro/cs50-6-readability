from cs50 import get_string
import string
import re

text = get_string("Text: ")

count_letters = 0

for letters in text.lower():
    if letters in string.ascii_lowercase:
        count_letters += 1

words = re.split(r" ", text)

sentences = re.split(r"[.?!]", text)

L = (100 * count_letters) / len(words)
S = (100 * (len(sentences) - 1)) / len(words)

index = 0.0588*L - 0.296*S - 15.8

r_index = round(index)

if r_index >= 16:
    print("Grade 16+")
elif r_index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {r_index}")
