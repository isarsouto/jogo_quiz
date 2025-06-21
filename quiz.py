def obter_perguntas(categoria):
     if categoria == "1":
         return [
             {
                 "pergunta": "Qual é a capital do Brasil?",
                 "opcoes": ["A) São Paulo", "B) Brasília", "C) Rio de Janeiro", "D) Belo Horizonte"],
                 "resposta": "B"
             },
             {
                 "pergunta": "Qual linguagem estamos usando?",
                 "opcoes": ["A) Python", "B) Java", "C) HTML", "D) C++"],
                 "resposta": "A"
             },
         ]
     elif categoria =="2":
         return [
             {
                 "pergunta": "Quanto é 2 + 2 * 2?",
                 "opcoes": ["A) 6", "B) 8", "C) 4", "D) 10"],
                 "resposta": "A"
             },
             {
                 "pergunta": "Tomate é:",
                 "opcoes": ["A) Legume", "B) Fruta", "C) Raiz", "D) Verdura"],
                 "resposta": "B"
             }
         ]
     elif categoria == "3":  # Curiosidades
         return [
             {
                 "pergunta": "Quem criou o Python?",
                 "opcoes": ["A) Elon Musk", "B) Linus Torvalds", "C) Guido van Rossum", "D) Bill Gates"],
                 "resposta": "C"
             },
             {
                 "pergunta": "Tomate é:",
                 "opcoes": ["A) Legume", "B) Fruta", "C) Raiz", "D) Verdura"],
                 "resposta": "B"
             }
         ]
     else:
         return[]

def jogar():
    while True:
        print("\n🧠 Escolha a categoria:")
        print("1 - Geral")
        print("2 - Matemática")
        print("3 - Curiosidades")

        categoria = input("Digite o número da categoria: ").strip()

        perguntas = obter_perguntas(categoria)

        if not perguntas:
            print("❌ Categoria inválida!")
            return

        pontos = 0
        print("\n🎯 Iniciando o quiz...\n")

        for i, p in enumerate(perguntas):
            print(f"Pergunta {i + 1}: {p['pergunta']}")
            for opcao in p["opcoes"]:
                print(opcao)

            resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()

            if resposta == p["resposta"]:
                print("✅ Resposta correta!\n")
                pontos += 1
            else:
                print(f"❌ Errado! A resposta certa era: {p['resposta']}\n")

        print(f"🏁 Fim do quiz! Você acertou {pontos} de {len(perguntas)} perguntas.")
        salvar_historico(pontos, len(perguntas), categoria)

        # NOVO: perguntar se quer jogar novamente
        jogar_novamente = input("🔁 Deseja jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente != "S":
            break

def salvar_historico(pontos, total, categoria):
    nomes = {"1": "Geral", "2": "Matemática", "3": "Curiosidades"}
    nome_categoria = nomes.get(categoria, "Desconhecida")
    with open("historico_quiz.txt", "a") as arquivo:
        arquivo.write(f"Categoria: {nome_categoria}  | Acertos: {pontos}/{total}\n")

def mostrar_historico():
    print("\n📜 Histórico de pontuações:")
    try:
       with open("historico_quiz.txt", "r") as arquivo:
           conteudo = arquivo.read()
           if conteudo.strip() == "":
               print("Nenhum jogo registrado ainda.")
           else:
               print(conteudo)
    except FileNotFoundError:
        print("Nenhum histórico encontrado ainda.")
    print()

def menu():
    while True:
        print("===== MENU QUIZ =====")
        print("1 - Jogar")
        print("2 - Ver historico")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            jogar()
        elif escolha =="2":
            mostrar_historico()
        elif escolha == "3":
            print("👋 Até a próxima!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.\n")


menu()
