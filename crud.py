#Properstar#
propriedades = {
    "Casa Verde": {
        "tipo": "Casa",
        "metros_quadrados": 120.5,
        "preco_venda": 350000.0,
        "preco_aluguel": 1800.0,
        "status": "Disponível",
    },
    "Apto Centro": {
        "tipo": "Apartamento",
        "metros_quadrados": 65.0,
        "preco_venda": 280000.0,
        "preco_aluguel": 1500.0,
        "status": "Disponível",
    },
    "Sobrado Sol": {
        "tipo": "Sobrado",
        "metros_quadrados": 150.75,
        "preco_venda": 420000.0,
        "preco_aluguel": 2300.0,
        "status": "Disponível",
    },
    "Cobertura Mar": {
        "tipo": "Cobertura",
        "metros_quadrados": 210.0,
        "preco_venda": 950000.0,
        "preco_aluguel": 5500.0,
        "status": "Disponível",
    },
    "Chacara Lago": {
        "tipo": "Chácara",
        "metros_quadrados": 800.0,
        "preco_venda": 500000.0,
        "preco_aluguel": 2800.0,
        "status": "Disponível",
    },
}

rodando = True

while rodando:
    print("\n===== PROPERSTAR =====")
    print("1 - Ver lista de propriedades")
    print("2 - Buscar propriedade por nome")
    print("3 - Comprar propriedade")
    print("4 - Alugar propriedade")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Propriedades ---")
        for nome, dados in propriedades.items():
            print(f"{nome} ({dados['tipo']}) - {dados['metros_quadrados']:.2f} m²")
            print(f"    Venda: R$ {dados['preco_venda']:.2f} | Aluguel: R$ {dados['preco_aluguel']:.2f}/mês")
            print(f"    Status: {dados['status']}")

    elif opcao == "2":
        busca = input("Digite o nome exato da propriedade: ")
        if busca in propriedades:
            dados = propriedades[busca]
            print("\nPropriedade encontrada:")
            print(f"{busca} ({dados['tipo']})")
            print(f"Área: {dados['metros_quadrados']:.2f} m²")
            print(f"Venda: R$ {dados['preco_venda']:.2f}")
            print(f"Aluguel: R$ {dados['preco_aluguel']:.2f}/mês")
            print(f"Status: {dados['status']}")
        else:
            print("Propriedade não encontrada.")

    elif opcao == "3":
        busca = input("Nome da propriedade que deseja comprar: ")
        if busca in propriedades:
            dados = propriedades[busca]
            if dados["status"] == "Disponível":
                print(f"Valor da compra: R$ {dados['preco_venda']:.2f}")
                confirma = input("Confirmar compra? (s/n): ")
                if confirma == "s":
                    dados["status"] = "Vendida"
                    print(f"Parabéns! Você comprou {busca}.")
                else:
                    print("Compra cancelada.")
            else:
                print(f"Indisponível. Status atual: {dados['status']}.")
        else:
            print("Propriedade não encontrada.")

    elif opcao == "4":
        busca = input("Nome da propriedade que deseja alugar: ")
        if busca in propriedades:
            dados = propriedades[busca]
            if dados["status"] == "Disponível":
                meses = int(input("Por quantos meses? "))
                if meses > 0:
                    total = dados["preco_aluguel"] * meses
                    print(f"Total do aluguel: R$ {total:.2f} ({meses} meses)")
                    confirma = input("Confirmar aluguel? (s/n): ")
                    if confirma == "s":
                        dados["status"] = "Alugada"
                        print(f"Você alugou {busca} por {meses} meses.")
                    else:
                        print("Aluguel cancelado.")
                else:
                    print("Quantidade de meses inválida.")
            else:
                print(f"Indisponível. Status atual: {dados['status']}.")
        else:
            print("Propriedade não encontrada.")

    elif opcao == "0":
        print("Até logo!")
        rodando = False

    else:
        print("Opção inválida. Tente novamente.")