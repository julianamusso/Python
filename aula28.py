﻿name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

if name and age:
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")

    if " " in name:
        print(f"Seu nome contém espaços")
    else:
        print(f"Seu nome não contém espaços")

    print(f"Seu nome tem {len(name)} letras")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A última letra do seu nome é {name[-1]}")   
else:
    print("Desculpe, você deixou campos vazios")