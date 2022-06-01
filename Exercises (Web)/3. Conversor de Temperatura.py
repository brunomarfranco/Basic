user_input = (input("Digite uma temperatura acompanhada da letra F (Fahrenheit) ou C (Celsius) para conversão: "))
degree = float(user_input[:-1])
unit = user_input[-1].upper()


def temperature(num):
    if unit == "C":
        fahrenheit = (9 * num + 160) / 5
        fahrenheit = round(fahrenheit)
        return f'{fahrenheit}ºF'
    elif unit == "F":
        celsius = (5 * num - 160) / 9
        celsius = round(celsius)
        return f'{celsius}ºC'


print(temperature(degree))
