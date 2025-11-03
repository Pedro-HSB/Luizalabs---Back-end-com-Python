class Usuario:
    def __init__(self, nome, dt_nasc, cpf, endereco):
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.cpf = cpf
        self.endereco = endereco
        
    def __repr__(self):
        return f'Usuario(nome={self.nome!r}, data_nascimento={self.dt_nasc!r}, cpf={self.cpf!r}, endereco={self.endereco!r})'


class Conta_corrente:
    def __init__(self, agencia, conta, usuario, numero_saques, limite_saque, limite_conta_corrente, saldo_conta_corrente, extrato):
        self.agencia = agencia
        self.conta = conta
        self.usuario = usuario
        self.numero_saques = numero_saques
        self.limite_saque = limite_saque
        self.limite_conta_corrente = limite_conta_corrente
        self.saldo_conta_corrente = saldo_conta_corrente
        self.extrato = extrato
        
    def __repr__(self):
        # Exibindo uma versão compacta da conta corrente
        return (f'Conta_corrente(agencia={self.agencia!r}, conta={self.conta!r}, usuario={self.usuario!r}, '
                f'numero_saques={self.numero_saques!r}, limite_saque={self.limite_saque!r}, '
                f'limite_conta_corrente={self.limite_conta_corrente!r}, saldo_conta_corrente={self.saldo_conta_corrente!r})')

    def extrato_completo(self):
        # Método para exibir o extrato completo, por exemplo
        return f'Conta {self.conta} - Extrato: {self.extrato}'

    # Métodos para retornar cada atributo
    def retorna_agencia(self):
        return self.agencia

    def retorna_conta(self):
        return self.conta

    def retorna_numero_saques(self):
        return self.numero_saques

    def retorna_limite_saque(self):
        return self.limite_saque

    def retorna_limite_conta_corrente(self):
        return self.limite_conta_corrente

    def retorna_saldo_conta_corrente(self):
        return self.saldo_conta_corrente



def sacar(*,saldo, valor, numero_saques, usuario_cadastrado) :
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > usuario_cadastrado.limite_conta_corrente
    excedeu_saques = numero_saques >= usuario_cadastrado.limite_saque
    
    if excedeu_saldo:
        return print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        return print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        return print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        usuario_cadastrado.saldo_conta_corrente -= valor
        usuario_cadastrado.extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return usuario_cadastrado.extrato,saldo, numero_saques
    else:
        print("Operação falhou! O valor informado é inválido.")
        return usuario_cadastrado.extrato,saldo, numero_saques
    
    
def depositar(saldo, valor, extrato, usuario, /):

    if valor > 0:
        saldo += valor
        usuario.saldo_conta_corrente += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        usuario_cadastrado.extrato += extrato
        return extrato, saldo
    else:
        print("Operação falhou! O valor informado é inválido.")
        return extrato, saldo


def exibe_extrato(saldo, /,*, extrato_cliente, nome):
    extrato_formatado = "\n================ EXTRATO ================"
    extrato_formatado += f"\n============== Cliente {nome} ========="
    extrato_formatado += "\n" + ("Não foram realizadas movimentações." if not extrato_cliente else extrato_cliente)
    extrato_formatado += f"\nSaldo: R$ {saldo:.2f}"
    extrato_formatado += "\n=========================================="
    return extrato_formatado    
    
def cria_usuario():
    nome_usuario = input("Informe o nome do usuario: ")
    dt_nasc_usuario = input("Informe a data de nascimento do usuario: ")
    cpf_usuario = input("Informe o cpf do usuario: ")
    endereco_usuario = input("Informe o endereco do usuario: ")
    usuario_cadastrado = any(cliente.cpf_conta_corrente == cpf_usuario for cliente in lista_cliente)
    if usuario_cadastrado : return 'Esse Usuario Já Existe no Sistema'
    usuario_informado = Usuario(nome_usuario, dt_nasc_usuario, cpf_usuario, endereco_usuario)
    lista_cliente.append(usuario_informado)
    return lista_cliente


def verifica_usuario(cpf_usuario):
    usuario_cadastrado = any(cliente.cpf_conta_corrente == cpf_usuario for cliente in lista_cliente)
    if usuario_cadastrado : return next((cliente for cliente in lista_cliente if cliente.cpf_conta_corrente == cpf_usuario), None)
    else : return 'Esse Usuario não Existe no Sistema'
    
def cria_conta_corrente(ultimo_digito_conta_corrente):
    cpf_usuario = input("Informe o cpf do usuario: ")
    usuario_cadastrado = any(cliente.cpf == cpf_usuario for cliente in lista_cliente)
    # numero_saques_usuario = input("Informe o numero de saques para usuario: ")
    # limite_saque_usuario = input("Informe o limite de saque do usuario: ")
    # limite_conta_corrente_usuario = input("Informe o limite do usuario: ")
    # saldo_conta_corrente_usuario = input("Informe o saldo do usuario: ")
    numero_saques_usuario = 5
    limite_saque_usuario = 5
    limite_conta_corrente_usuario = 1000
    saldo_conta_corrente_usuario = 100
    ultimo_digito_conta_corrente += 1
    extrato = ''
    if usuario_cadastrado : 
        conta_corrente_informada = Conta_corrente(AGENCIA, ultimo_digito_conta_corrente, cpf_usuario,numero_saques_usuario, limite_saque_usuario, limite_conta_corrente_usuario, saldo_conta_corrente_usuario, extrato)
        return lista_conta_corrente.append(conta_corrente_informada)
        # return Conta_corrente(AGENCIA, ultimo_digito_conta_corrente, cpf_usuario,numero_saques_usuario, limite_saque_usuario, limite_conta_corrente_usuario, saldo_conta_corrente_usuario, extrato)
    else : 
        return 'Usuario não localizado'
    
    
    
   
usuario_logado = None
lista_cliente = []
lista_conta_corrente = []
saldo = 0
ultimo_digito_conta_corrente = 0
AGENCIA = '0001'
numero_saques = 0
inicia_usuario = """


[1] Cria Usuario

[2] Utilizar Usuario Ja Cadastrado


=> """

while True:

    opcao = input(inicia_usuario)

    if opcao == "1":
        usuario_logado = cria_usuario()
        break
    elif opcao == "2":
        cpf_usuario = input("Informe o cpf do usuario: ")
        usuario_logado = verifica_usuario(cpf_usuario)
        if usuario_logado != "":
            print(f"{usuario_logado}")

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
# usuario_cadastrado = any(clientes.usuario == usuario_logado.cpf for clientes in lista_conta_corrente)

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cria Conta Corrente
[5] Sair

=> """

while True:

    opcao = input(menu)
    usuario_cadastrado = next((cliente for cliente in lista_conta_corrente if cliente.usuario == usuario_logado[0].cpf), None)

    if opcao == "1":
        if usuario_cadastrado == None : 
            print('Conta Corrente Não localizada')
        else:
            valor = float(input("Informe o valor do depósito: "))
            depositar(usuario_cadastrado.saldo_conta_corrente, valor, usuario_cadastrado.extrato, usuario_cadastrado)
    elif opcao == "2":
        if usuario_cadastrado == None : 
            print('Conta Corrente Não localizada')
        else:
            valor = float(input("Informe o valor do saque: "))
            sacar(saldo=usuario_cadastrado.saldo_conta_corrente, valor=valor, numero_saques=numero_saques, usuario_cadastrado=usuario_cadastrado)
    elif opcao == "3":
        if usuario_cadastrado == None : 
            print('Conta Corrente Não localizada')
        else:
            retorno_extrato = exibe_extrato(usuario_cadastrado.saldo_conta_corrente, extrato_cliente=usuario_cadastrado.extrato, nome=usuario_logado[0].nome)
            print(retorno_extrato)
    elif opcao == "4":
        retorno_cria_conta = cria_conta_corrente(ultimo_digito_conta_corrente)
        if retorno_cria_conta != "":
            print(retorno_cria_conta)

    elif opcao == "5":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
