import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "desenvolvimento", "jogo"]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    print(estagios[tentativas])

def jogo_da_forca():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_adivinhadas = set()

    print("Bem-vindo ao jogo da forca!")
    
    while tentativas < 6:
        exibir_forca(tentativas)
        print("Palavra: " + " ".join(palavra_oculta))
        print("\nLetras adivinhadas: " + ", ".join(letras_adivinhadas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente novamente.")
            continue

        letras_adivinhadas.add(letra)

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            if "_" not in palavra_oculta:
                print("Parabéns! Você adivinhou a palavra:", palavra)
                break
        else:
            tentativas += 1

    if "_" in palavra_oculta:
        exibir_forca(tentativas)
        print("Você perdeu! A palavra era:", palavra)

# Executando o jogo da forca
jogo_da_forca()
