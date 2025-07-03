import textwrap
import datetime   


def menu():
    menu = f"""
    ================ MENU ================
    Saldo atual: R$ {saldo:.2f}
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

n_limite_saque = 3
limite_saque = 500
numero_saques_efetuado = 0
data_hoje = datetime.date.today().strftime("%d/%m/%Y")

saldo = 0.0
extrato = ""
historico_saques = []
historico_depositos = []

print("Bem-vindo ao sistema bancário!")
print("Data de hoje:", data_hoje)


def depositar(saldo, valor_deposito):
    
    saldo += valor_deposito
    historico_depositos.append({
                "data": data_hoje,
                "valor": valor_deposito
            })
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
     
    print(f"Saldo após depósito: R$ {saldo:.2f}")
    return saldo

def sacar(saldo, valor_saque, numero_saques_efetuado):
    if valor_saque > saldo:
        print("Saldo insuficiente")
    elif valor_saque < 0:
        print("Valor inválido")
    elif numero_saques_efetuado >= n_limite_saque:
        print("Limite de saques atingido")
    elif valor_saque > limite_saque:
        print("Valor do saque maior que o limite")
    else:
        saldo -= valor_saque
        numero_saques_efetuado += 1
        historico_saques.append({
            "data": data_hoje,
            "valor": valor_saque
        })
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        print(f"Saldo após saque: {saldo:.2f}")
    return saldo, numero_saques_efetuado

while True:
    opcao = menu()
    
    if opcao == 'd':
        valor_deposito = float(input("Qual valor você quer depositar? "))
        if valor_deposito > 0:
            saldo = depositar(saldo, valor_deposito)

        else:
            print("Valor inválido para depósito.")

    elif opcao == 's':
        valor_saque = float(input("Qual valor do saque? "))
        if valor_saque > 0:
            saldo, numero_saques_efetuado = sacar(saldo, valor_saque, numero_saques_efetuado)
        else:
            print("Valor inválido para saque.")

    elif opcao == 'e':
        # Exibir extrato
        print("Exibindo extrato...")
        # Verifica se há movimentações
        if not historico_depositos and not historico_saques:
            print(f"""
            ================ EXTRATO ================
            Deposito(s):
            \tNão foram realizadas movimentações.
            Saque(s):
            \tNão foram realizadas movimentações.
            Saques efetuados/Limite de saques:
            \t{numero_saques_efetuado}/{n_limite_saque}
            ==========================================
            Saldo:\t\tR$ {saldo:.2f}
            ==========================================
            """)
            continue
        # Verifica se há depósitos
        # Formatação do extrato com histórico de depósitos e saques
        extrato = """
        ================ EXTRATO ================
        Deposito(s):
        \t{historico_depositos}
        Saque(s):
        \t{historico_saques}
        Saques efetuados/Limite de saques:
        \t{numero_saques_efetuado}/{n_limite_saque}
        ==========================================
        Saldo:\t\tR$ {saldo:.2f}
        ==========================================
        """
        print(extrato.format(
            historico_depositos="\t".join([f"{d['data']}: R$ {d['valor']:.2f}\n\t" for d in historico_depositos]) if historico_depositos else "Nenhum depósito realizado.",
            historico_saques="\t".join([f"{s['data']}: R$ {s['valor']:.2f}\n\t" for s in historico_saques]) if historico_saques else "Nenhum saque realizado.",
            numero_saques_efetuado=numero_saques_efetuado,
            n_limite_saque=n_limite_saque,
            saldo=saldo
        ))

    elif opcao == 'q':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, por favor tente novamente.")
# Fim do loop principal