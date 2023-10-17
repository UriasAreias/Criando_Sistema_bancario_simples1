menu = """
________________________________
[1] Deposito
[2] Saque
[3] Extrato
[9] Sair
________________________________
"""
extrato = ""
saldo = 0
saque = 0
LIMITE_DIARIO = 500
SAQUE_DIARIO = 3
numero_saque = 0

while True:
    opcao = input(menu)

    if opcao == "9":
        print("Sua operação foi finalizada. Obrigado pela preferência.")
        break

    elif opcao == "1":
        deposito = float(input("Digite o valor do Depósito: R$"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("Valor inválido, operação cancelada, tente novamente. Obrigado")
    
    elif opcao == "2":
        saque = float(input("Digite o valor do saque: R$ "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > LIMITE_DIARIO

        excedeu_saque = numero_saque >= SAQUE_DIARIO 

        if excedeu_saldo:
            print("Operação Falhou, saldo insuficiente.")

        elif excedeu_limite:
            print("Operação Falhou, Você exedeu o limite diario.")
        
        elif excedeu_saque:
            print("Operação Falhou, limete diario exedido.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saque += 1

        else:
            print("Valor inválido, operação cancelada, tente novamente. Obrigado")

    elif opcao == "3":

        print(f"seu saldo é de: R$ {saldo:.2f}")


