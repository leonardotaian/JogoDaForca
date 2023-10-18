from math import isnan
from dicionario import dic
import random, time



repetidas = ["init"]

aleat = random.randint(0, 100)

palavra = (dic[aleat])
quant_letras = len(palavra)

print("Que os jogos comecem...")

print("")
print("A palavra a qual você terá que descobrir tem",quant_letras,"letras")
print("Você terá exatamente",quant_letras,"chances para descobrir, acredito que seja o suficiente.")
print("Boa sorte!")

x = quant_letras

while x >= 0:

  tentativa = str(input("Tente uma letra: "))
  repetidas.append(tentativa)
  numero = any(char.isdigit() for char in tentativa)
  
  if repetidas.count(tentativa) == 1:
      print("Letra Repetida")
      repetidas.pop()
      x = x + 1
  elif len(tentativa) >= 2:
    print("Olha o golpe KKKKKKK é só uma letra!")
    repetidas.pop()
    x = x + 1
  elif bool(numero) == True:
    print("Tá achando que tá num bingo? Digite uma letra")
    repetidas.pop()
    x = x + 1
  else:
    x = x - 1

