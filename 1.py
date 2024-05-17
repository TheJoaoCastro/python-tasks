exit = False
contatos = {}

while exit == False:
    print("| Selecione a ação desejada |")
    print("")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Sair")

    opcao = input("Digite a opção: ")

    if opcao == "3":
        exit = True

    elif opcao == "1":
        print("")
        print("___________________________________")
        print("")
        nome = input("Digite o nome para o novo contato: ")
        numero = input("Digite o número do novo contato: ")
        contatos[nome] = numero
    
    elif opcao == "2":
        print("")
        print("___________________________________")
        print("")
        ctt = input("Nome do contato: ")
        print("Número: " + contatos[ctt])

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
