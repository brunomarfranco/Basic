word_phrase = input("Digite uma palavra ou frase: ").lower()
final_string = word_phrase.replace(" ", "",).replace("'", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace("\"", "").replace("-", "").replace(".", "").replace("~", "")
final_string_rev = final_string[::-1]

if final_string == final_string_rev:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")


def final_string(1):

