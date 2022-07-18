user_input = input("Digite uma frase de pelo menos 4 palavras: ")


def reverse_order(phrase):

    words_list = phrase.split()

    if len(words_list) >= 4:
        reverse_list = words_list[::-1]
        reverse_phrase = " ".join(reverse_list)
        return reverse_phrase
    else:
        print("A frase precisa ter pelo menos 4 palavras!")


print(reverse_order(user_input))
