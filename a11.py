def preco():
    print ('1-salgado  ')
    print ('2-refrigerante ')
    print ('3-suco ')
    print ('4-sorvete ')
    print ("5-cafe ")
    print ("6-capuccino ")
    print ("7-bolo  ")
    print ("8-dadinho")
    pedido = int(input("Qual o produto cujo o preço deve ser consultado?(digite apenas os numeros): "))
    if pedido == 1:
        print ('R$ 4,00')
    if pedido == 2:
        print ('R$ 4,50')
    if pedido == 3:
        print ('R$ 5,00')
    if pedido == 4:
        print ('R$ 6,00')
    if pedido == 5:
        print ('R$ 4,00')
    if pedido == 6:
        print ('R$ 6,00')
    if pedido == 7:
        print ('R$ 4,50')
    if pedido == 8:
        print ('R$ 4,50')


preco()
