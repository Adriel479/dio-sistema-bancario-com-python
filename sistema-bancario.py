from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

    def __str__(self):
        output = ""
        for transacao in self._transacoes:
            if transacao.__class__.__name__ == "Saque":
                output += f" - R${transacao.valor}\n"
            else:
                output += f" + R${transacao.valor}\n"
        return output

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor 

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor 

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(self)

class Conta(ABC):
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor 
            return True 
        return False 
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor 
            return True 
        return False 

    @classmethod
    @abstractmethod
    def nova_conta(cls, cliente, numero):
        pass

class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        self._cliente = cliente 
        self._numero = numero
        self._limite = 500
        self._limite_saques = 3
        self._saldo = 0
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if self._limite_saques ==  0:
            return False
        if valor > self._limite:
            return False
        if self._saldo < valor:
            return False
        self._limite_saques -= 1
        self._saldo -= valor
        return True
    
    def __str__(self):
        return f" Agencia: 0001\n Número: {self._numero}\n Saldo: R$ {self._saldo:.2f}\n Histórico:\n{self.historico}"
    
class Cliente:
    def __init__(self, nome, cpf, endereco):
        self._nome = nome 
        self._cpf = cpf
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def __str__(self):
        aux = ""
        for conta in self._contas:
            aux += f"{conta}"
        return f"Nome: {self._nome}\nCPF: {self._cpf}\nEndereço: {self._endereco}\nContas:\n{aux}"


c = Cliente("Usuário", "12345678910", "Rua A, 123, Bairro, Cidade - AA")
cc = ContaCorrente.nova_conta(c, 123)
c.adicionar_conta(cc)
c.realizar_transacao(cc, Deposito(200))
c.realizar_transacao(cc, Deposito(200))
c.realizar_transacao(cc, Deposito(300))
c.realizar_transacao(cc, Saque(100))
c.realizar_transacao(cc, Saque(100))
c.realizar_transacao(cc, Saque(100))
c.realizar_transacao(cc, Saque(100))
print(c)