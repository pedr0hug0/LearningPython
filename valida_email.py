import sys
# Entrada do usuário
email = input().strip()
#verificar se é um email válido
if '@' in email and '.' in email.split('@')[-1]:
    print("Email válido")
else:
    print("Email inválido")