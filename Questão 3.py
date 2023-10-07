print("Bem-vindo ao PetShop do Gustavo Henrique Francisco da Silva!")

# Função para calcular o valor base de acordo com o peso do cachorro:
def cachorro_peso():
    while True:
        try:
            peso = float(input("Entre com o peso do cachorro: "))
            if peso < 3:
                return 40
            elif 3 <= peso < 10:
                return 50
            elif 10 <= peso < 30:
                return 60
            elif 30 <= peso < 50:
                return 70
            else:
                print("Não aceitamos cachorros tão grandes. \nPor favor entre com o peso do cachorro novamente.\n")
        except ValueError:
            print("Você digitou um valor não numérico. \nPor favor entre com o peso do cachorro novamente.\n")


# Função para definir o multiplicador de acordo com o tipo de pelo do cachorro:
def cachorro_pelo():
    while True:
        pelo = input("\nEntre com o pelo do cachorro:\nc - Pelo Curto\nm - Pelo Médio\nl - Pelo Longo\n>> ")
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção inválida. Por favor, digite 'c' para pelo curto, 'm' para pelo médio ou 'l' para pelo longo.")


# Função para calcular o valor extra com base nos serviços adicionais
def cachorro_extra():
    valor_extra = 0
    while True:
        try:
            adicional = int(input("\nDeseja adicionar mais algum serviço? \n1 - Corte de Unhas - R$ 10,00 \n2 - Escovar Dentes - R$ 12,00 \n3 - Limpeza de Orelhas - R$ 15,00 \n0 - Não desejo mais nada. \n>> "))
            if adicional == 0:
                return valor_extra
            elif adicional == 1:
                valor_extra += 10
            elif adicional == 2:
                valor_extra += 12
            elif adicional == 3:
                valor_extra += 15
            else:
                print("Opção inválida. Por favor, escolha um serviço adicional válido.")
        except ValueError:
            print("Valor inválido. Por favor, escolha um serviço adicional válido.")

# Um "Try" onde é feito o cálculo do valor total usando o peso, o tipo de pelo e os serviços adicionais e em seguida
# retorna o total a pagar na tela.
try:
    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    valor_extra = cachorro_extra()

    total = base * multiplicador + valor_extra
    print(f"Total a pagar(R$): {total:.2f} (peso: {base} * pelo: {multiplicador} + adicional(is): {valor_extra}")
except:
    print("Ocorreu um erro inesperado.")

