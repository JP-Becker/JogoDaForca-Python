import random

def escolher_palavra():
    palavras = ["python", "programacao", "estudo", "jogo", "forca", "teste", "pc"]
    return random.choice(palavras)

def exibir_estado_atual(palavra, letras_adivinhadas):
    return " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_restantes = 6
    letras_erradas = set()

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas_restantes > 0:
        print(f"\nPalavra: {exibir_estado_atual(palavra, letras_adivinhadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {' '.join(letras_erradas)}")

        tentativa = input("Adivinhe uma letra: ").lower()

        if tentativa in letras_adivinhadas or tentativa in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if tentativa in palavra:
            letras_adivinhadas.add(tentativa)
            if set(palavra) == letras_adivinhadas:
                print(f"\nParabéns! Você adivinhou a palavra: {palavra}")
                break
        else:
            letras_erradas.add(tentativa)
            tentativas_restantes -= 1

        if tentativas_restantes == 0:
            print(f"\nGame over! A palavra era: {palavra}")

if __name__ == "__main__":
    jogo_da_forca()