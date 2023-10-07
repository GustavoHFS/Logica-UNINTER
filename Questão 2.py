# Cardápio da Sorveteria
print('Bem vindo a Sorveteria do Gustavo Henrique Francisco da Silva')
print('---------------------------------------Cardápio--------------------------------------------')
print('|  Nº DE BOLAS  |  Sabor Tradicional (tr)  |  Sabor Premium (pr)  |  Sabor Especial (es)  |')
print('|       1       |         R$ 6,00          |        R$ 7,00       |        R$ 8,00        |')
print('|       2       |         R$ 10,00         |        R$ 12,00      |        R$ 14,00       |')
print('|       3       |         R$ 14,00         |        R$ 17,00      |        R$ 20,00       |')
print('-------------------------------------------------------------------------------------------\n')

valor = 0
total = 0

# Onde é feito o pedido especificando a quantidade e o sabor em um loop que se quebra quando o que foi inserido
# é válido ou continua a perguntar quanto o dado é inválido
while True:
    while True:
        sabor = input('\nEntre com o sabor desejado ( tr / pr / es ): ')
        if sabor == 'tr' or sabor == 'pr' or sabor == 'es':
            bolas = input('Entre com o número de bolas de sorvete desejado ( 1 / 2 / 3 ): ')
            if bolas == '1' or bolas == '2' or bolas == '3':
                break
            else:
                print('Número de bolas de sorvete inválido. Tente novamente \n')
                continue
        else:
            print('Sabor inválido. Tente novamente\n')
            continue

# Na parte a seguir foi definido o valor de cada sabor de sorvete de acordo com a quantidade bolas
    if sabor == 'tr':
        if bolas == '1':
            valor = 6
        elif bolas == '2':
            valor = 10
        elif bolas == '3':
            valor = 14

    elif sabor == 'pr':
        if bolas == '1':
            valor = 7
        elif bolas == '2':
            valor = 12
        else:
            valor = 17

    elif sabor == 'es':
        if bolas == '1':
            valor = 8
        elif bolas == '2':
            valor = 14
        else:
            valor = 20

    if sabor == 'tr':
        print('Você pediu {} bolas de sorvete no sabor TRADICIONAL: R${},00 !'.format(bolas, valor))
    elif sabor == 'pr':
        print('Você pediu {} bolas de sorvete no sabor PREMIUM: R${},00 !'.format(bolas, valor))
    elif sabor == 'es':
        print('Você pediu {} bolas de sorvete no sabor ESPECIAL: R${},00 !'.format(bolas, valor))

# Aqui é feito o calculo do valor total das compras, em que a cada novo pedido de sorvete o valor é adicionado a variável "total"
    total += valor

    novacompra = input('Deseja mais algum sorvete ? (s/digite outra tecla): ')
    if novacompra == 's':
        continue
    else:
        break

#Mostrado na tela o valor total do pedido
print('\nO valor total a ser pago: R${},00'.format(total))