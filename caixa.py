saldo = 0.0

print ("=== Caixa Eletrônico! ===")

while True:
    print("\nMenu")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        valor = float(input("Digite um valor para depósito: R$"))
        saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "2":
        valor = float(input("Digite um valor para saque: R$"))
        if valor <= saldo:
            saldo-=valor
            print(f"saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque. Digite outro valor!")
    elif opcao == "3":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Saindo...")
        break

    else: 
        print("Opção inválida. Tente novamente!")            
