NUMERO_AGENCIA = "0001"
MAX_SAQUES_DIARIOS = 3
MAX_VALOR_SAQUE = 500
MENU = """
************ MENU ***********
* [d] Depósitar valor       * 
* [s] Sacar valor           *
* [e] Imprimir extrato      *
* [c] Cadastrar cliente     *
* [a] Cadastrar conta       *
* [l] Listar contas         *
* [i] Listar clientes       *
* [q] Sair do sistema       *
*****************************

Digite uma opção do menu: """

saldo = 0.0
extrato = ""
numero_saques_dia = 0

contas_banco = []
clientes_banco = []
sequencial_conta = 1

def exbir_menu(menu):
    return input(menu)
    
def depositar(saldo, valor, extrato): #Parâmetros exclusivamente posicionados. IN(saldo, valor, extrato), OUT(saldo, extrato).
    if valor > 0.0:
            saldo += valor
            valor_string = f"R${valor:.2f}|"
            valor_formatado = '{: >12}'.format(valor_string)
            extrato += f"|DEPÓSITO     |{valor_formatado}\n"
            print(f"Depósito no valor de R${valor:.2f} efetuado com sucesso.")
    else:
        print("Valor inválido, por favor digite um valor novamente.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato): #Parâmetros exclusivamente nomeados. IN(saldo, valor, extrato), OUT(saldo, extrato).
    global numero_saques_dia
    if numero_saques_dia >= MAX_SAQUES_DIARIOS:
        print("Número de saques diários excedido.")
    else:
        if valor > MAX_VALOR_SAQUE:
            print("O valor máximo para saque é de R$500.00.")
        else:
            if valor > 0:
                if saldo - float(valor) < 0:
                    print(f"\nSaldo insuficiente! Seu saldo é de:{saldo:.2f}")
                else:
                    saldo -= float(valor)
                    numero_saques_dia += 1
                    valor_string = f"R${valor:.2f}|"
                    valor_formatado = '{: >12}'.format(valor_string)
                    extrato += f"|SAQUE        |{valor_formatado}\n"
                    print(f"Saque no valor de R${valor:.2f} efetuado com sucesso. Saques ainda permitidos hoje: {MAX_SAQUES_DIARIOS - numero_saques_dia}.")
            else:
                print("Valor inválido, por favor digite um valor novamente.")
    return saldo, extrato

def gravar_extrato(linha):
    global extrato
    extrato += linha

def imprimir_extrato(saldo, *, extrato): #Parâmetro posicionado (saldo), parâmetro nomeado (extrato). 
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
            
def cadastrar_cliente(clientes_banco):
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente. (Somente números): ")
    while True:
        for pessoa in clientes_banco:
            if pessoa.get(cpf, {}) != {}:
                cpf = input("Já existe um cliente com esse CPF informado. Por favor informe outro CPF. (Somente números): ")
            else:
                break
        break
    data_nascimento = input("Informe a data de nascimento do cliente. (Formato <dd/mm/yyyy>): ")
    logradouro, numero, cidade, uf = input("Informe o endereço do cliente. (Formato: <logradouro>, <número>, <cidade>, <estado>): ").split(",")
    cliente = {cpf: {"nome":nome, "nascimento":data_nascimento, "endereco": f"{' '.join(logradouro.split())}, {numero.strip()} - {' '.join(cidade.split())}/{uf.strip()}"}}
    clientes_banco.append(cliente)
    print(f"Cliente <{nome}> cadastrado com sucesso.")
    return cpf

def cadastrar_conta(clientes_banco, contas_banco):
    global sequencial_conta
    sucesso = False
    clientes_banco_local = clientes_banco.copy()
    if len(clientes_banco) == 0:
        cpf = cadastrar_cliente(clientes_banco)
    else:
        cpf = input("Por favor informe o CPF do titular da conta: ")
    while not sucesso:
        for pessoa in clientes_banco_local:
            if pessoa.get(cpf, {}) != {}:
                conta = {"agencia":NUMERO_AGENCIA, "conta":sequencial_conta, "titular": cpf}
                contas_banco.append(conta)
                sequencial_conta += 1
                print(f"Conta do cliente <{pessoa[cpf]['nome']}> cadastrada com sucesso.")
                sucesso = True
                break
            cpf = input("O CPF informado não pertence a nenhum de nossos clientes. Por favor informe outro CPF. (Somente números): ")

def listar_contas(clientes_banco, contas_banco):
    if len(contas_banco) == 0:
        print("\nNenhuma conta foi cadastrada no sistema ainda.", end = "")
    else:
        for conta in contas_banco:
            titular_conta = next((pessoa for pessoa in clientes_banco if conta["titular"] in pessoa), None)
            print(f"\nAgência: {NUMERO_AGENCIA} / Conta: {conta['conta']} / Titular: {titular_conta[conta['titular']]['nome']}", end = "")
    print()

def listar_clientes(clientes_banco):
    if len(clientes_banco) == 0:
        print("\nNenhum cliente foi cadastrado no sistema ainda.", end = "")
    else:
        for pessoa in clientes_banco:
            for cpf, dados in pessoa.items():
                print(f"\nCliente: {dados['nome']} / CPF: {cpf}", end = "")
    print()
           
def main():
    global saldo, extrato, numero_saques_dia, sequencial_conta, contas_banco, clientes_banco
    while True:
        opcao = exbir_menu(MENU)
        if opcao =="d":
            valor = float(input("\nInforme o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("\nInforme o valor que deseja sacar: "))
            saldo, extrato = sacar(saldo = saldo, valor = valor, extrato = extrato)
        elif opcao == "e":
            imprimir_extrato(saldo, extrato = extrato)
        elif opcao == "c":
            cadastrar_cliente(clientes_banco)
        elif opcao == "a":
            cadastrar_conta(clientes_banco, contas_banco)
        elif opcao == "l":
            listar_contas(clientes_banco, contas_banco)
        elif opcao == "i":
            listar_clientes(clientes_banco)
        elif opcao == "q":
            print("\nObrigado por utilizar o nosso banco!\n")
            break
        else:
            print("\nOperação inválida, por favor escolha uma opção novamente!")
            
main()
