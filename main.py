from dicionario import dic
import random

repetidas = []
aleat = random.randint(0, 100)
palavra = dic[aleat].strip()
quant_letras = len(palavra)

print("Que os jogos comecem...")
print(f"\nA palavra a qual você terá que descobrir tem {quant_letras} letras.")
print(f"Você terá exatamente {quant_letras} chances para descobrir a palavra. Boa sorte!\n")

for i in range(quant_letras):
    tentativa = input("Tente uma letra: ").strip().lower()
    if tentativa in repetidas:
        print("Letra Repetida")
        
    elif len(tentativa) != 1 or not tentativa.isalpha():
        print("Tá tentando dar o golpe? Apenas uma letra e tem que ser válida.")
        
    else:
        repetidas.append(tentativa)
        if tentativa in palavra:
            print("Acertou!")
        else:
            print("Furada.")

print("\nFim do jogo. A palavra era:", palavra)

