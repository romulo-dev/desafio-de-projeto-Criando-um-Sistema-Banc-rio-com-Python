import datetime


extrato = ""
saldoCliente = 0.00
dataUltimoSaque = None
numeroSaques = 0


while True:

    print("D - para depositar")
    print("S - para sacar")
    print("E - para tirar extrato")
    print("Q - para sair")
    opcao = str(input("Selecione uma opcao: "))

    if opcao == "D":
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito > 0.00:
            DataDeposito = datetime.datetime.today()
            saldoCliente += deposito
            extrato += f"Deposito de R${deposito :.2f} feito em {DataDeposito}\n"
        else:
            print("Você não digitou o valor corretamente")
    elif opcao == "S":
        saque = float(input("Digite o valor a ser sacado: "))
        dataSaque = datetime.datetime.today()
        if saque > 0.00 and saque <= saldoCliente and type(saque) == float and saque <= 500.00:
            if dataUltimoSaque is None:
               dataUltimoSaque = datetime.datetime.today()
               numeroSaques += 1
               saldoCliente -= saque 
               extrato += f"Saque de R${saque:.2f} realizado em {dataUltimoSaque}\n"
            else: 
                if dataSaque.date() >=  dataUltimoSaque.today().date():
                    if numeroSaques == 3:
                        print("vc já atingiu o seu limite de saques por dia")
                    else:
                        numeroSaques += 1
                        dataUltimoSaque = dataSaque
                        saldoCliente -= saque
                        extrato += f"Saque de R${saque:.2f} realizado em {dataUltimoSaque}\n"
                else:
                    print("Ocorreu um erro")
        else:
            print("Você digitou 0 ou um valor negativo ou seu saldo não é suficiente para esse saque ou você digitou um valor inválido")
    elif opcao == "E":
        print(extrato)
    elif opcao == "Q":
        print("Saindo...")
        break
    else:
        print("Você digitou um caractere inválido")
