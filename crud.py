nomes = ["Casa Verde", "Apto Centro", "Sobrado Sol", "Cobertura Mar", "Chacara Lago"]
tipos = ["Casa", "Apartamento", "Sobrado", "Cobertura", "Chácara"]
precos_venda = [350000.0, 280000.0, 420000.0, 950000.0, 500000.0]
precos_aluguel = [1800.0, 1500.0, 2300.0, 5500.0, 2800.0]
status = ["Disponível", "Disponível", "Disponível", "Disponível", "Disponível"]

rodando = True

while rodando:
    print("\n===== IMOBILIÁRIA =====")
    print("1 - Ver lista de propriedades")
    print("2 - Buscar propriedade por nome")
    print("3 - Comprar propriedade")
    print("4 - Alugar propriedade")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

   
    if opcao == "1":
        print("\n--- Propriedades ---")
        i = 0
        while i < len(nomes):
            print(f"[{i}] {nomes[i]} ({tipos[i]})")
            print(f"    Venda: R$ {precos_venda[i]:.2f} | Aluguel: R$ {precos_aluguel[i]:.2f}/mês")
            print(f"    Status: {status[i]}")
            i += 1

   
    elif opcao == "2":
        busca = input("Digite o nome exato da propriedade: ")
        if busca in nomes:
            pos = nomes.index(busca)
            print(f"\nEncontrada na posição {pos}:")
            print(f"{nomes[pos]} ({tipos[pos]})")
            print(f"Venda: R$ {precos_venda[pos]:.2f}")
            print(f"Aluguel: R$ {precos_aluguel[pos]:.2f}/mês")
            print(f"Status: {status[pos]}")
        else:
            print("Propriedade não encontrada.")

    
    elif opcao == "3":
        busca = input("Nome da propriedade que deseja comprar: ")
        if busca in nomes:
            pos = nomes.index(busca)
            if status[pos] == "Disponível":
                print(f"Valor da compra: R$ {precos_venda[pos]:.2f}")
                confirma = input("Confirmar compra? (s/n): ")
                if confirma == "s":
                    status[pos] = "Vendida"
                    print(f"Parabéns! Você comprou {nomes[pos]}.")
                else:
                    print("Compra cancelada.")
            else:
                print(f"Indisponível. Status atual: {status[pos]}.")
        else:
            print("Propriedade não encontrada.")

 
    elif opcao == "4":
        busca = input("Nome da propriedade que deseja alugar: ")
        if busca in nomes:
            pos = nomes.index(busca)
            if status[pos] == "Disponível":
                meses = int(input("Por quantos meses? "))
                if meses > 0:
                    total = precos_aluguel[pos] * meses
                    print(f"Total do aluguel: R$ {total:.2f} ({meses} meses)")
                    confirma = input("Confirmar aluguel? (s/n): ")
                    if confirma == "s":
                        status[pos] = "Alugada"
                        print(f"Você alugou {nomes[pos]} por {meses} meses.")
                    else:
                        print("Aluguel cancelado.")
                else:
                    print("Quantidade de meses inválida.")
            else:
                print(f"Indisponível. Status atual: {status[pos]}.")
        else:
            print("Propriedade não encontrada.")


    elif opcao == "0":
        print("Até logo!")
        rodando = False

    else:
        print("Opção inválida. Tente novamente.")
