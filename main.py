Pontos = 0
Senha = input("Digite sua senha: ")

if len(Senha) <=8:
    Pontos += 0

#tamanho da senha
if len(Senha) > 8 and len(Senha) <= 12:
    Pontos += 1

if len(Senha) > 12:
    Pontos += 2

#Tipos de Caracteres
if any(char.isdigit() for char in Senha):
    Pontos += 1

if any(char.isupper() for char in Senha):
    Pontos += 1

if any(char.islower() for char in Senha):
    Pontos += 1

if any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in Senha):
    Pontos += 1


if Pontos <= 2:
    print("Senha muito fraca")
elif Pontos <= 4:
    print("Senha fraca")
elif Pontos <= 5:
    print("Senha Média")
elif Pontos == 6:
    print("Senha Forte")
else: 
    print("Senha Muito Forte")
