cd from math import isnan
import random
import time

dic = ['dicionário', 'intrínseco', 'prescindir', 'presunçoso', 'diligência', 'corroborar', 'intempérie', 'detrimento', 'maturidade', 'parcimônia', 'referência', 'inspiração', 'inexorável', 'pragmático', 'prepotente', 'incipiente', 'disruptivo', 'sororidade', 'serenidade', 'arbitrário', 'indulgente', 'auspicioso', 'iniquidade', 'pertinente', 'sagacidade', 'resignação', 'hipocrisia', 'preconizar', 'precedente', 'vislumbrar', 'incidência', 'lisonjeado', 'suscetível', 'entretanto', 'disposição', 'excêntrico', 'subestimar', 'preliminar', 'tribulação', 'depreender', 'fleumático', 'anacrônico', 'equivocado', 'retrógrado', 'indolência', 'escrutínio', 'excelência', 'ingerência', 'democracia', 'infortúnio', 'compassivo', 'contemplar', 'restringir', 'importante', 'pejorativo', 'sintetizar', 'proposição', 'primordial', 'signatário', 'conjuntura', 'coercitivo', 'dissolução', 'finalidade', 'itinerário', 'subjacente', 'intrínseca', 'esplêndido', 'alteridade', 'entanto', 'pecuniária', 'espontâneo', 'designação', 'transeunte', 'necessário', 'constância', 'sarcástico', 'pusilânime', 'desprovido', 'privilégio', 'idoneidade', 'verossímil', 'pernóstico', 'exacerbado', 'felicidade', 'relevância', 'divergente', 'disciplina', 'inferência', 'pernicioso', 'disseminar', 'satisfação', 'meticuloso', 'reverberar', 'esporádico', 'influência', 'militância', 'consolidar', 'retumbante', 'subversivo', 'fornicação']
repetidas = []

# print(len(dic[0])) verificando o tamanho da string
# print(dic[0].find()) para verificar se tem uma letra na string

aleat = random.randint(0, 100)

palavra = (dic[aleat])
quant_letras = len(palavra)

print("Que os jogos comecem...")
print("")
print("A palavra a qual você terá que descobrir tem",quant_letras,"letras")
print("Você terá exatamente",quant_letras,"chances para descobrir, acredito que seja o suficiente.")
print("Boa sorte!")

for x in range(10):

  tentativa = input("Tente uma letra: ")

  if repetidas.count(tentativa) == 1:
    print("Essa letra já foi parceiro, tenta outra")
    repetidas.pop()

  repetidas.append(tentativa)

  if len(tentativa) >= 2:
    print("É apenas uma letra, estou de olho em você")
    repetidas.pop()

  numero = any(char.isdigit() for char in tentativa)

  if bool(numero) == True:
    print("Tá achando que tá num bingo? Digita uma letra")
    repetidas.pop()

