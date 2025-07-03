import sys
# Entrada do usuário
email = input().strip()
#verificar se é um email válido  
# Regras para um e-mail válido:
#Deve conter o caractere "@" e um domínio, como "gmail.com" ou "outlook.com".
#Não pode começar ou terminar com "@".
#Não pode conter espaços.
if "@" in email and "." in email.split("@")[-1] and not email.startswith("@") and not email.endswith("@") and " " not in email:
    print("E-mail válido")
else:
    print("E-mail inválido")
