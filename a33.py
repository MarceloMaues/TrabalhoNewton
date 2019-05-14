def nome(): 
    print ('1-salgado  ')
    print ('2-refrigerante ')
    print ('3-suco ')
    print ('4-sorvete ')
    print ("5-cafe ")
    print ("6-capuccino ")
    print ("7-bolo  ")
    print ("8-dadinho")
    print ("Digite o número dos pedidos na hora de pedir")
    nome = str(input("Qual o seu nome: "))
    pedido = str(input("Qual o pedido: "))
    nome2 = str(input("Qual o seu nome: "))
    pedido2 = str(input("Qual o pedido: "))
    nome3 = str(input("Qual o seu nome: "))
    pedido3 = str(input("Qual o pedido: "))
    nome4 = str(input("Qual o seu nome: "))
    pedido4 = str(input("Qual o pedido: "))
    nome5 = str(input("Qual o seu nome: "))
    pedido5 = str(input("Qual o pedido: "))
    nome6 = str(input("Qual o seu nome: "))
    pedido6 = str(input("Qual o pedido: "))
    nome7 = str(input("Qual o seu nome: "))
    pedido7 = str(input("Qual o pedido: "))
    name = []
    name.append(nome)
    name.append(nome2)
    name.append(nome3)
    name.append(nome4)
    name.append(nome5)
    name.append(nome6)
    name.append(nome7)
    itens = []
    itens.append(pedido)
    itens.append(pedido2)
    itens.append(pedido3)
    itens.append(pedido4)
    itens.append(pedido5)
    itens.append(pedido6)
    itens.append(pedido7)
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


nome()
