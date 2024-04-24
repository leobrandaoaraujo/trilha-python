MAX_SAQUES_DIARIOS = 3
MAX_VALOR_SAQUE = 500

saldo = 0.0
extrato = ""
numero_saques_dia = 0

menu = """
******* MENU *******
* [d] Depósito     * 
* [s] Saque        *
* [e] Extrato      *
* [q] Sair         *
********************

Digite uma opção: """

while True:
    opcao = input(menu)
    if opcao =="d":
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0.0:
            saldo += valor
            valor_string = f"R${valor:.2f}|"
            valor_formatado = '{: >12}'.format(valor_string)
            extrato += f"|DEPÓSITO     |{valor_formatado}\n"
            print(f"Depósito no valor de R${valor:.2f} efetuado com sucesso.")
        else:
            print("Valor inválido, por favor digite um valor novamente.")
    elif opcao == "s":
        if numero_saques_dia >= MAX_SAQUES_DIARIOS:
            print("Número de saques diários excedido.")
        else:
            valor = float(input("Informe o valor que deseja sacar: "))
            if valor > MAX_VALOR_SAQUE:
                print("O valor máximo para saque é de R$500.00.")
            else:
                if valor > 0:
                    if saldo - float(valor) < 0:
                        print(f"Saldo insuficiente! Seu saldo é de:{saldo:.2f}")
                    else:
                        saldo -= float(valor)
                        numero_saques_dia += 1
                        valor_string = f"R${valor:.2f}|"
                        valor_formatado = '{: >12}'.format(valor_string)
                        extrato += f"|SAQUE        |{valor_formatado}\n"
                        print(f"Saque no valor de R${valor:.2f} efetuado com sucesso. Saques ainda permitidos hoje: {MAX_SAQUES_DIARIOS - numero_saques_dia}.")
                else:
                    print("Valor inválido, por favor digite um valor novamente.")
    elif opcao == "e":
        saldo_string = f"SALDO: R${saldo:.2f}|"
        saldo_formatado = "|" + '{: >26}'.format(saldo_string)
        if not extrato:
            print("---------------------------")
            print(saldo_formatado)
            print("---------------------------")
        else:
            print("""
---------------------------
|          EXTRATO        |
--------------------------
|OPERAÇÃO     |      VALOR|
---------------------------""")
            print(extrato, end = "")
            print("---------------------------")
            print(saldo_formatado)
            print("---------------------------")
    elif opcao == "q":
        print("Obrigado por utilizar o nosso banco!\n")
        break
    else:
        print("Operação inválida, por favor escolha uma opção novamente!")
