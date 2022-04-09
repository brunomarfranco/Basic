full_name = input("Digite seu nome completo: ")
all_names = full_name.split()
last = ""

for surname in range(len(all_names)):
    last = all_names[surname]

print("Seu nome é last")


