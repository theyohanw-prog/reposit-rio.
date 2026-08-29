nome = João

nota1 = 9.5
nota2 = 8.0
nota3 = 7.5
nota4 = 10.0

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 0 and media <= 4:
    situacao = "Reprovado"
    elif media >= 5 and media <= 6:
        situacao = "Recuperação"
        elif media >= 7 and media <= 10:
            situacao = "Aprovado"
            else:
                situacao = "Média inválida"

        
                print("\n--- RESULTADO ---")
                print("Aluno:", nome)
                print("Média final:", round(media, 2))
                print("Situação:", situacao)