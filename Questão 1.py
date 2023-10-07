print('\nBem-vindo a Loja do Gustavo Henrique Francisco da Silva')

# Solicita o preço do produto e sua quantidade e atribui as suas respectivas variáveis.
preco = float(input('\nEntre com o valor do produto: R$'))
quant = int(input('Entre com a quantidade do produto: '))

# Multiplicando o preço que foi inserido pela quantidade do produto para achar o valor total da compra.
total = preco * quant

if preco > 0 and quant > 0:

    # O método usado para aplicar o desconto foi utilizando a fórmula: [valor total * (desconto / 100)] para achar
    # o valor à ser descontado e em seguida subtrair esse resultado do valor total original.
    if quant < 200:
        print('\nO valor SEM desconto: R${}'.format(total))
        print('O valor COM desconto: R${}'.format(total))
    elif 200 <= quant < 1000:
        print('\nO valor SEM desconto: R${}'.format(total))
        print('O valor COM desconto: R${}'.format(total - (total * (5 / 100))))
    elif 1000 <= quant < 2000:
        print('\nO valor SEM desconto: R${}'.format(total))
        print('O valor COM desconto: R${}'.format(total - (total * (10 / 100))))
    elif 2000 <= quant:
        print('\nO valor SEM desconto: R${}'.format(total))
        print('O valor COM desconto: R${}'.format(total - (total * (15 / 100))))

