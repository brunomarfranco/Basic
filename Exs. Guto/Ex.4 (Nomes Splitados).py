full_name = input("Digite seu nome completo: ")
first = full_name.split()[0]
last = ""

for name in range(len(full_name.split())):
    if name == 1:
        last = last + full_name.split()[name]
    if name > 1:
        last = last + " " + full_name.split()[name]

if len(full_name.split()) > 1:
    print(f'Seu nome é {first} e seu sobrenome é {last}')
else:
    print(f'Seu nome é {first}')
