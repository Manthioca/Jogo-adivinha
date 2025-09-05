import random
import time

def jogar_adivinhacao():
    # --- Configuração Inicial ---
    print("=========================================")
    print("  Bem-vindo ao Jogo de Adivinhação!  ")
    print("=========================================")

    # --- Escolha de Dificuldade ---
    while True:
        print("\nEscolha o nível de dificuldade:")
        print("(1) Fácil (1-50, 10 tentativas)")
        print("(2) Médio (1-100, 7 tentativas)")
        print("(3) Difícil (1-500, 5 tentativas)")
        
        nivel_str = input("Digite o número do nível: ")
        if nivel_str == '1':
            limite_maximo = 50
            total_tentativas = 10
            break
        elif nivel_str == '2':
            limite_maximo = 100
            total_tentativas = 7
            break
        elif nivel_str == '3':
            limite_maximo = 500
            total_tentativas = 5
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

    # --- Início do Jogo ---
    numero_secreto = random.randint(1, limite_maximo)
    print(f"\nEu pensei em um número entre 1 e {limite_maximo}. Você tem {total_tentativas} tentativas.")
    time.sleep(1) # Pequena pausa para dar um efeito

    # --- Loop de Tentativas ---
    for tentativa_atual in range(1, total_tentativas + 1):
        print(f"\n--- Tentativa {tentativa_atual} de {total_tentativas} ---")
        
        try:
            palpite_str = input("Qual é o seu palpite? ")
            palpite = int(palpite_str)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número. Você perdeu uma tentativa!")
            continue # Pula para a próxima iteração do loop

        # Validação do intervalo do palpite
        if palpite < 1 or palpite > limite_maximo:
            print(f"Palpite fora do intervalo! Digite um número entre 1 e {limite_maximo}.")
            continue

        # Comparação e Dicas
        if palpite == numero_secreto:
            print(f"🎉 PARABÉNS! Você acertou em {tentativa_atual} tentativas! O número era {numero_secreto}.")
            break # Encerra o jogo pois o jogador acertou
        elif palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        else:
            print("Muito alto! Tente um número menor.")
        
        # Verifica se as tentativas acabaram
        if tentativa_atual == total_tentativas:
            print("\nGAME OVER! Suas tentativas acabaram.")
            print(f"O número secreto era {numero_secreto}.")

def jogar_novamente():
    while True:
        jogar_adivinhacao()
        
        resposta = input("\nDeseja jogar novamente? (s/n): ").lower()
        if resposta != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    jogar_novamente()