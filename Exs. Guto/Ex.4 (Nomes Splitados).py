full_name = input("Digite seu nome completo: ")
all_names = full_name.split()
all_surnames = all_names[1:]

if len(all_names) > 0:
    first = all_names[0]
    last = " ".join(all_surnames)

    if len(all_names) > 1:
        print(f'Seu nome é {first} e seu sobrenome é {last}')
    else:
        print(f'Seu nome é {first}')

else:
    print("Digite um nome válido!")