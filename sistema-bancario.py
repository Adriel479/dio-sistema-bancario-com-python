def depositar(valor):
    global saldo, extrato
    if valor <= 0:
        print("O valor do depósito deve ser maior que zero.")
        return
    saldo += valor
    extrato += f"Depósito R$ {valor:10.2f}".center(TAMANHO_TEXTO, " ") + "\n"

def sacar(valor):
    global saldo, extrato, numero_saques
    if valor <= 0:
        print("O valor do saque é inválido.")
        return 
    if valor > saldo:
        print("O valor do saque é maior que o valor do saldo.")
        return 
    if valor > limite:
        print("Você só pode sacar R$ 500,00 por vez.")
        return 
    if numero_saques == LIMITE_SAQUES:
        print(f"Você só pode realizar {LIMITE_SAQUES} saques diários.")
        return
    saldo -= valor 
    numero_saques += 1 
    extrato += f"Saque    R$ {valor:10.2f}".center(TAMANHO_TEXTO, " ") + "\n"
    
def exibir_extrato():
    titulo = "EXTRATO".center(TAMANHO_TEXTO, "-")
    print(titulo)
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    print(extrato)
    print(f"Saldo    R$ {saldo:10.2f}".center(TAMANHO_TEXTO, " "))
    print(''.center(len(titulo), '-'))

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
TAMANHO_TEXTO = 30

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor: "))
        depositar(valor)
    elif opcao == "s":
        valor = float(input("Informe o valor: "))
        sacar(valor)
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")