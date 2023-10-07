# Função para cadastrar um novo colaborador
def cadastrar_colaborador(id):
    print("******************************************************************************")
    print("-------------------------MENU CADASTRAR COLABORADOR---------------------------")
    print(f"id do colaborador {id_global}")
    nome = input("Por favor entre com o nome: ")
    setor = input("Por favor entre com o setor: ")
    pagamento = float(input("Por favor entre com o pagamento (R$): "))

    colaborador = {"ID": id, "Nome": nome, "Setor": setor, "Pagamento": pagamento}
    lista_colaboradores.append(colaborador)
    print("Colaborador cadastrado com sucesso!")


# Função para consultar colaboradores
def consultar_colaborador():
    while True:
        print("******************************************************************************")
        print("-------------------------MENU CONSULTAR COLABORADOR---------------------------")
        print("Opções de consulta:")
        print("1 - Consultar Todos os Colaboradores")
        print("2 - Consultar Colaborador por ID")
        print("3 - Consultar Colaborador(es) por setor")
        print("4 - Retornar.")

        opcao = input(">> ")

        if opcao == "1":
                for colaborador in lista_colaboradores:
                    print("---------------------------------------")
                    print(f"ID: {colaborador['ID']}\nNome: {colaborador['Nome']}\nSetor: {colaborador['Setor']}\nPagamento: R$ {colaborador['Pagamento']:.2f}")
                    print("---------------------------------------")
        elif opcao == "2":
            id_colaborador = int(input("Digite o ID do colaborador: "))
            encontrado = False
            for colaborador in lista_colaboradores:
                if colaborador["ID"] == id_colaborador:
                    print("---------------------------------------")
                    print(f"ID: {colaborador['ID']}\nNome: {colaborador['Nome']}\nSetor: {colaborador['Setor']}\nPagamento: R$ {colaborador['Pagamento']:.2f}")
                    print("---------------------------------------")
                    encontrado = True
                    break
            if not encontrado:
                print("Colaborador não encontrado.")
        elif opcao == "3":
            setor = input("Digite o setor do(s) colaborador(es): ")
            for colaborador in lista_colaboradores:
                if colaborador["Setor"] == setor:
                    print("---------------------------------------")
                    print(f"ID: {colaborador['ID']}\nNome: {colaborador['Nome']}\nSetor: {colaborador['Setor']}\nPagamento: R$ {colaborador['Pagamento']:.2f}")
                    print("---------------------------------------")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


# Função para remover um colaborador
def remover_colaborador():
    print("******************************************************************************")
    print("--------------------------MENU REMOVER COLABORADOR----------------------------")
    id_colaborador = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["ID"] == id_colaborador:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso!")
            return
    print("Colaborador não encontrado.")


# Variáveis globais
lista_colaboradores = []
id_global = 1

#Menu Principal com cada opção disponível
print("Bem-vindo ao Controle de Colaboradores do Gustavo Henrique Francisco da Silva!")
while True:
    print("******************************************************************************")
    print("-------------------------------MENU PRINCIPAL---------------------------------")
    print("1 - Cadastrar Colaborador")
    print("2 - Consultar Colaborador(es)")
    print("3 - Remover Colaborador")
    print("4 - Sair.")
    opcao = input(">> ")

    if opcao == "1":
        cadastrar_colaborador(id_global)
        id_global += 1
    elif opcao == "2":
        consultar_colaborador()
    elif opcao == "3":
        remover_colaborador()
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
