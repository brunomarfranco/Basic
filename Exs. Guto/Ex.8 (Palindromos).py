import unidecode
import re

raw_sentence = input("Digite uma palavra ou frase: ")
processed_sentence = unidecode.unidecode(raw_sentence).lower()
processed_sentence = re.sub("[^a-z0-9]", "", processed_sentence)
reversed_sentence = processed_sentence[::-1]

if processed_sentence == reversed_sentence:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

# unidecode.unidecode transforma a frase Unicode em ASCII, retirando acentos e demais caracteres não presentes em ASCII
# lower() transforma letras maiúsculas em minúsculas
# re.sub transforma tudo que não for letras minúsculas de a-z e nºs de 0-9 em uma string vazia (ou seja, remove-as)
# então está removendo espaços, vírgulas, exclamações, entre outros caracteres que existem em ASCII
