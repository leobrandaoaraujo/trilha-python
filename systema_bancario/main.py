from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import string
import functools
import re
from pathlib import Path

MENU = """
************ MENU ***********
* [d] Depositar valor       * 
* [s] Sacar valor           *
* [c] Cadastrar cliente     *
* [a] Cadastrar conta       *
* [i] Listar clientes       *
* [l] Listar contas         *
* [e] Extrato completo      *
* [es] Extrato de saques    *
* [ed] Extrato de depósitos *
* [o] Listar log            *
* [q] Sair do sistema       *
*****************************

Digite uma opção do menu: """

ROOT_PATH = Path(__file__).parent
sequencial_conta = 1
log_operacoes = []

def exbir_menu(menu):
    return input(menu)

def log_operacao(func):
    global log_operacoes
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        now = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        retorno = func(*args, **kwargs)
        log_operacoes.append(f"Log: Função \"{func.__name__}\" executada em {now}.")
        try:
            with open(ROOT_PATH / "log.txt", "a", encoding="utf-8") as log:
                log.write(f"[{now}] Função {func.__name__} executada com os argumentos ({", ".join(re.sub("[\\[\\]]", "", str(arg)) for arg in args)}){" e (" + kwargs +")" if len(kwargs) > 0 else ""} e retornando {retorno}.\n")
        except IOError:
            print("Erro ao tentar abrir o arquivo de log.")
        return retorno
    return envelope
    
def main():
    global log_operacoes
    
    contas_banco = []
    clientes_banco = []
  
    while True:
        opcao = exbir_menu(MENU)
        if opcao =="d" or opcao == "s" or opcao == "e" or opcao == "es" or opcao == "ed":
            cpf = input("\nInforme o CPF do cliente. (Somente números): ")
            cliente = buscar_cliente(cpf, clientes_banco)
            if not cliente:
                print("\nO CPF informado não pertence a nenhum de nossos clientes.")
                continue
            else:
                if len(cliente.contas) == 0:
                    print(f"\nSr(a) {cliente.nome}, você ainda não possui nenhuma conta no banco.")
                    continue
                
                if opcao =="d" or opcao == "s":
                    numero_conta = input(f"\nOlá Sr(a) {cliente.nome}, por favor informe o número da sua conta onde deseja realizar o {"depósito" if opcao=="d" else "saque"}: ")
                else:
                    numero_conta = input(f"\nOlá Sr(a) {cliente.nome}, por favor informe o número da sua conta que deseja imprimir o extrato: ")
                
                conta = buscar_conta(cliente, numero_conta)
                
                if not conta:
                    print("\nA conta com o número informado não foi encontrada na sua relação de contas.")
                    continue
                else:
                    if opcao =="d" or opcao == "s":
                        valor = float(input(f"\nConta de nº {conta.numero} encontrada. Agora, informe o valor que deseja {"depositar" if opcao=="d" else "sacar"}: "))
                        transacao = Deposito(valor) if opcao=="d" else Saque(valor)
                        cliente.realizar_transacao(conta, transacao)
                    else:
                        if  opcao == "e":
                            imprimir_extrato(conta)
                        elif opcao == "es":
                            imprimir_extrato(conta, "saque")
                        else:
                            imprimir_extrato(conta, "deposito")
        elif opcao == "c":
            cadastrar_cliente(clientes_banco)
        elif opcao == "a":
            cadastrar_conta(clientes_banco, contas_banco)
        elif opcao == "l":
            listar_contas(contas_banco)
        elif opcao == "i":
            listar_clientes(clientes_banco)
        elif opcao == "o":
            listar_log(log_operacoes)
        elif opcao == "q":
            print("\nObrigado por utilizar o nosso banco!\n")
            break
        else:
            print("\nOperação inválida, por favor escolha uma opção novamente!")
            
def buscar_cliente(cpf, clientes):
    cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None

def buscar_conta(cliente, numero_conta):
    conta = [conta for conta in cliente.contas if int(conta.numero) == int(numero_conta)]
    return conta[0] if conta else None

@log_operacao
def cadastrar_cliente(clientes_banco) -> Cliente:
    cpf_liberado = False
    nome = input("Informe o nome do cliente: ")
    cpf = input("Informe o CPF do cliente. (Somente números): ")
    if len(clientes_banco) > 0:
        while not cpf_liberado:
            for pessoa in clientes_banco:
                if pessoa.cpf != cpf:
                    cpf_liberado = True
                else:
                    cpf = input("Já existe um cliente com esse CPF informado. Por favor informe outro CPF. (Somente números): ")
                    cpf_liberado = False
                    break
    data_nascimento = input("Informe a data de nascimento do cliente. (Formato <dd/mm/yyyy>): ")
    logradouro, numero, cidade, uf = input("Informe o endereço do cliente. (Formato: <logradouro>, <número>, <cidade>, <estado>): ").split(",")
    cliente = PessoaFisica(cpf.replace(" ", ""), string.capwords(" ".join(nome.split())), data_nascimento.replace(" ", ""), endereco=f"{" ".join(logradouro.split())}, {" ".join(numero.split()) if numero else "S/N"}, {" ".join(cidade.split())}-{uf.strip().upper()}")
    clientes_banco.append(cliente)
    print(f"Cliente <{string.capwords(" ".join(nome.split()))}> cadastrado com sucesso.")
    return cliente

@log_operacao
def cadastrar_conta(clientes_banco, contas_banco):
    global sequencial_conta
    sucesso = False
    if len(clientes_banco) == 0:
        novo_cliente = cadastrar_cliente(clientes_banco)
        cpf = novo_cliente.cpf
    else:
        cpf = input("Por favor informe o CPF do titular da conta: ")
    while not sucesso:
        for cliente in clientes_banco:
            if cliente.cpf == cpf:
                conta = Conta(sequencial_conta, cliente)
                cliente.adicionar_conta(conta)
                contas_banco.append(conta)
                sequencial_conta += 1
                print(f"Conta do cliente <{cliente.nome}> cadastrada com sucesso.")
                sucesso = True
                break
            cpf = input("O CPF informado não pertence a nenhum de nossos clientes. Por favor informe outro CPF. (Somente números): ")

@log_operacao
def imprimir_extrato(conta, tipo_transacao=None):
    saldo_string = f"SALDO: R${conta.saldo:.2f}|"
    saldo_formatado = "|" + saldo_string.rjust(48)
    transacoes = conta.historico.gerar_relatorio(tipo_transacao)
    if not transacoes:
        print()
        print("-------------------------------------------------")
        print(saldo_formatado)
        print("-------------------------------------------------")
    else:
        extrato = ""
        for transacao in transacoes:
            valor_string = f"R${float(transacao["valor"]):.2f}|"
            valor_formatado = valor_string.rjust(12)
            extrato += f"|{transacao["tipo"].upper().ljust(13)}|{valor_formatado}{transacao["data"].strftime("%d/%m/%Y %H:%M:%S").center(21)}|\n"
        
        print(f"""
-------------------------------------------------
|{"EXTRATO DA CONTA".center(47) if not tipo_transacao else "EXTRATO DE SAQUES".center(47) if tipo_transacao.lower() == "saque" else "EXTRATO DE DEPÓSITOS".center(47)}|
-------------------------------------------------
|OPERAÇÃO     |      VALOR|      DATA/HORA      |
-------------------------------------------------""")
        print(extrato, end = "")
        print("-------------------------------------------------")
        if not tipo_transacao:
            print(saldo_formatado)
            print("-------------------------------------------------")
        
def listar_contas(contas_banco):
    if len(contas_banco) == 0:
        print("\nNenhuma conta foi cadastrada no sistema ainda.", end = "")
    else:
        for conta in IteradorConta(contas_banco):
            print(f"\nAgência: {conta.agencia} / Conta: {conta.numero} / Titular: {conta.cliente.nome}", end = "")
    print()

def listar_clientes(clientes_banco):
    if len(clientes_banco) == 0:
        print("\nNenhum cliente foi cadastrado no sistema ainda.", end = "")
    else:
        for pessoa in clientes_banco:
            print(f"\nCliente: {pessoa.nome} / CPF: {pessoa.cpf}", end = "")
    print()

def listar_log(log_operacoes):
    print()
    print(" LOG DE OPERAÇÕES ".center(70 , "-"))
    for log in log_operacoes:
        print(log)
    print("-".center(70 , "-"))

class Conta():
    def __init__(self, numero, cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._max_transacoes_diarias = 10
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<Ag: {self._agencia} - Nro: {self._numero}>" 
                
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> float:
        return self._numero

    @property
    def agencia(self) -> float:
        return self._agencia

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def historico(self) -> float:
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero) -> Conta:
        return cls(numero, cliente)
    
    @log_operacao
    def sacar(self, valor) -> bool:
        saldo_insuficiente = valor > self._saldo
        transacoes_diarias_excedidas = self._historico.trasacoes_do_dia >= self._max_transacoes_diarias
        
        if transacoes_diarias_excedidas:
            print(f"\nO número máximo de {self._max_transacoes_diarias} transações diárias já foi atingido.")
        elif saldo_insuficiente:
            print(f"\nSaldo insuficiente! Seu saldo é de:{self._saldo:.2f}")
        elif valor > 0:
            self._saldo -= valor
            print(f"Saque no valor de R${valor:.2f} efetuado com sucesso.")
            return True
        else:
            print("Valor inválido, por favor digite um valor novamente.")
        
        return False
    
    @log_operacao
    def depositar(self, valor) -> bool:
        saldo_atual = self._saldo
        transacoes_diarias_excedidas = self._historico.trasacoes_do_dia >= self._max_transacoes_diarias
        
        if transacoes_diarias_excedidas:
            print(f"\nO número máximo de {self._max_transacoes_diarias} transações diárias já foi atingido.")
        elif valor > 0:
            self._saldo += valor
            print(f"Depósito no valor de R${valor:.2f} efetuado com sucesso.")
            return True
        else:
            print("Valor inválido, por favor digite um valor novamente.")
        
        return False
    
class ContaCorrente(Conta):
    def __init__(self, limite=500, limite_saques=3, **kw) -> None:
        super().__init__(**kw)
        self._limite = limite
        self._limite_saques = limite_saques
        
    def __repr__(self) -> str:
        return f"{super().__class__.__name__}<Ag: {super()._agencia} - Nro: {super()._numero}>"
    
    def sacar(self, valor) -> bool:
        numero_saques_dia = len([transacao for transacao in self._historico.transacoes if transacao["tipo"] == Saque.__name__])
        limite_excedido = valor > self._limite
        limite_saques_excedido = numero_saques_dia > self._limite_saques
        
        if limite_saques_excedido:
            print("Número de saques diários excedido.")
        elif limite_excedido:
            print("O valor máximo para saque é de R$500.00.")
        else:
            return super().sacar(valor)
        
        return False

class IteradorConta():
    def __init__(self, contas: list[Conta]):
        self.contas = contas
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self.index]
            self.index += 1
            return conta 
        except IndexError:
            raise StopIteration
    
class Cliente:
    def __init__(self, endereco) -> None:
        self._endereco = endereco
        self._contas = []
        
    @property
    def endereco(self) -> str:
        return self._endereco
    
    @property
    def contas(self) -> list:
        return self._contas
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, **kw) -> None:
        super().__init__(**kw)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<CPF: {self._cpf}>"
        
    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento
        
class Historico():
    def __init__(self) -> None:
        self._transacoes = []
         
    @property
    def transacoes(self) -> list:
        return self._transacoes
    
    @property
    def trasacoes_do_dia(self) -> int:
        return len([transacao for transacao in self._transacoes if transacao["data"].date() == datetime.now().date()])
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": datetime.now()})
        
    def gerar_relatorio(self, tipo_transacao=None):
        if not tipo_transacao:
            return self._transacoes
        else:
            return [transacao for transacao in self._transacoes if transacao["tipo"].lower() == tipo_transacao.lower()]
        
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass 

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass
        
class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_ok = conta.depositar(self.valor)
        
        if transacao_ok:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        transacao_ok = conta.sacar(self.valor)
        
        if transacao_ok:
            conta.historico.adicionar_transacao(self)

main()
