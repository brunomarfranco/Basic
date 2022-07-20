import unidecode
import re

raw_sentence = input("Digite uma palavra ou frase: ")
processed_sentence = unidecode.unidecode(raw_sentence).lower()
processed_sentence = re.sub("[^a-z0-9]", "", processed_sentence)

palindromo = True

for left_index in range(len(processed_sentence) // 2):
    right_index = len(processed_sentence) - left_index - 1
    if processed_sentence[left_index] != processed_sentence[right_index]:
        palindromo = False

if palindromo:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
