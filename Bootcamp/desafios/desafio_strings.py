# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
print("Digite o preço do produto:")
preco = float(input().strip())

print("Digite o cupom de desconto:")
cupom = input().strip()

if cupom in descontos:
    preco_final = preco - (preco * descontos[cupom])
    print("Cupom válido")
    print("Preço final:")
    print(f"R$ {preco_final:.2f}")
else:
    print("Cupom inválido")
    print(f"{preco:.2f}")


# #Para passar pelo sistema de validação online, apenas saidas necessárias:
# import sys
# # Dicionário com os valores de desconto
# descontos = {
#     "DESCONTO10": 0.10,
#     "DESCONTO20": 0.20,
#     "SEM_DESCONTO": 0.00
# }

# # Entrada do usuário

# preco = float(sys.stdin.readline().strip())

# cupom = str(sys.stdin.readline().strip())


# if cupom in descontos:
#     preco_final = preco - (preco * descontos[cupom])
#     print(f"{preco_final:.2f}")
# else:
#     print(f"{preco:.2f}")