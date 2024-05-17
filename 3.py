exit = False
products = {}

while exit == False:
    print("| Menu |")
    print("")
    print("1. Adicionar produto")
    print("2. Atualizar produto")
    print("3. Consultar produto")
    print("4. Imprimit estoque")
    print("0. Sair")

    opcao = input("Digite a opção: ")

    if opcao == "0":
        exit = True

    elif opcao == "1":
        print("")
        print("___________________________________")
        print("")
        nome = input("Digite o nome do produto: ")
        valor = input("Digite seu valor: ")
        products[nome] = valor

    elif opcao == "2":
        print("")
        print("___________________________________")
        print("")
        nome = input("Digite o nome do produto: ")
        valor = input("Digite seu novo valor: ")
        products[nome] = valor

    elif opcao == "4":
        print("")
        print("___________________________________")
        print("")
        for product in products:
            print(products[product])
    
    elif opcao == "3":
        print("")
        print("___________________________________")
        print("")
        product = input("Digite o produto desejado: ")
        print("Valor: " + products[product])
    
    else:
        print("Opção inválida")

print("")
print("___________________________________")
print("")
print("")
print("        Programa encerrado")
print("")
print("")
print("___________________________________")
print("")

