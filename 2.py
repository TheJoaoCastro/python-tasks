exit = False
words = {}

while exit == False:
    print("| Tradutor Inglês <---> Português |")
    print("")
    print("1. Traduzir palavra")
    print("2. Adicionar nova palavra")
    print("3. Sair")

    opcao = input("Digite a opção: ")

    if opcao == "3":
        exit = True

    elif opcao == "2":
        print("")
        print("___________________________________")
        print("")
        p1 = input("Digite a palavra: ")
        p2 = input("Digite sua tradução: ")
        words[p1] = p2
        words[p2] = p1
    
    elif opcao == "1":
        print("")
        print("___________________________________")
        print("")
        word = input("Digite a palavra desejada: ")
        print("Tradução: " + words[word])
    
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

