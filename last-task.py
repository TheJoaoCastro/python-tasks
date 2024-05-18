exit = False
items = {}

while exit == False:
    print("| Itens |")
    print("")
    print("1. Adicionar item")
    print("2. Atualizar item")
    print("3. Excluir item")
    print("4. Ver itens")
    print("0. Sair")

    opcao = input("Digite a opção: ")

    if opcao == "0":
        exit = True

    elif opcao == "1":
        print("")
        print("___________________________________")
        print("")
        nome = input("Digite o nome do item: ")
        quantidade = input("Digite a quantidade: ")
        items[nome] = quantidade

    elif opcao == "2":
        print("")
        print("___________________________________")
        print("")
        nome = input("Digite o nome do item: ")
        quantidade = input("Digite a nova quantidade: ")
        items[nome] = quantidade
    
    elif opcao == "3":
        print("")
        print("___________________________________")
        print("")
        nome = input("Digite o nome do item para deletar: ")
        items.pop(nome)
        print("Deletado com sucesso!")

    elif opcao == "4":
        print("")
        print("___________________________________")
        print("")
        for item in items:
            print(item + ": " + items[item])

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

