from datetime import datetime 

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("O valor do depósito deve ser maior que zero.")
        return saldo, extrato
    saldo += valor
    extrato += f"Depósito R$ {valor:10.2f}".center(TAMANHO_TEXTO, " ") + "\n"
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("O valor do saque é inválido.")
        return saldo, extrato
    if valor > saldo:
        print("O valor do saque é maior que o valor do saldo.")
        return saldo, extrato
    if valor > limite:
        print("Você só pode sacar R$ 500,00 por vez.")
        return saldo, extrato
    if numero_saques == limite_saques:
        print(f"Você só pode realizar {limite_saques} saques diários.")
        return saldo, extrato
    saldo -= valor 
    numero_saques += 1 
    extrato += f"Saque    R$ {valor:10.2f}".center(TAMANHO_TEXTO, " ") + "\n"
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    titulo = "EXTRATO".center(TAMANHO_TEXTO, "-")
    print(titulo)
    if len(extrato) == 0:
        print("Não foram realizadas movimentações.")
    print(extrato)
    print(f"Saldo    R$ {saldo:10.2f}".center(TAMANHO_TEXTO, " "))
    print(''.center(len(titulo), '-'))

def adicionar_usuario(usuarios):
    nome = input("Nome: ")
    nascimento = datetime.strptime(input("Nascimento (dia/mes/ano): "), "%d/%m/%Y")
    cpf = input("CPF: ").replace("-","").replace(".", "")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário com este CPF!")
            return usuarios
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado(Sigla): ")
    if len(estado) != 2:
        print("Estado inválido!")
        return usuarios
    usuarios.append({"nome":nome, "nascimento": nascimento, "cpf": cpf, "endereco": f"{rua}, {numero} - {bairro} - {cidade}/{estado}"})
    return usuarios

def adicionar_conta(contador, contas, usuarios):
    cpf = input("CPF: ").replace("-","").replace(".", "")
    achei = False
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            achei = True 
            break
    if not achei:
        print("Usuário informado, não localizado.")
    contador += 1
    contas.append(dict(agencia="0001", conta=contador, cpf=cpf))
    return contador, contas


def listar_usuarios(usuarios, contas):
    titulo = "USUÁRIOS".center(TAMANHO_TEXTO, "-")
    print(titulo)
    for usuario in usuarios:
        print("  Nome:", usuario["nome"])
        print("  Nascimento:", usuario["nascimento"])
        print("  CPF:", usuario["cpf"])
        print("  Endereço:", usuario["endereco"])
        contas_usuario = ""
        for conta in contas:
            if conta["cpf"] == usuario["cpf"]:
                contas_usuario += f"   - Agencia: {conta['agencia']}, Conta: {conta['conta']}\n"
        if len(contas_usuario) > 0:
            print("  Contas:")
            print(contas_usuario)
    print(''.center(len(titulo), "-"))

menu = """

[u] Adicionar Usuário
[c] Adicionar Conta
[l] Listar Usuários
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
usuarios = []
contas = []
contador = 0

while True:
    opcao = input(menu)
    if opcao == "u":
        usuarios = adicionar_usuario(usuarios)
    elif opcao == "c":
        contador, contas = adicionar_conta(contador, contas, usuarios)
    elif opcao == "l":
        listar_usuarios(usuarios, contas)
    elif opcao == "d":
        valor = float(input("Informe o valor: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "s":
        valor = float(input("Informe o valor: "))
        saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")