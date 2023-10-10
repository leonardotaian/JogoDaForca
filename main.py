from math import isnan
import random
import time

dic = ['dicionário', 'intrínseco', 'prescindir', 'presunçoso', 'diligência', 'corroborar', 'intempérie', 'detrimento', 'maturidade', 'parcimônia', 'referência', 'inspiração', 'inexorável', 'pragmático', 'prepotente', 'incipiente', 'disruptivo', 'sororidade', 'serenidade', 'arbitrário', 'indulgente', 'auspicioso', 'iniquidade', 'pertinente', 'sagacidade', 'resignação', 'hipocrisia', 'preconizar', 'precedente', 'vislumbrar', 'incidência', 'lisonjeado', 'suscetível', 'entretanto', 'disposição', 'excêntrico', 'subestimar', 'preliminar', 'tribulação', 'depreender', 'fleumático', 'anacrônico', 'equivocado', 'retrógrado', 'indolência', 'escrutínio', 'excelência', 'ingerência', 'democracia', 'infortúnio', 'compassivo', 'contemplar', 'restringir', 'importante', 'pejorativo', 'sintetizar', 'proposição', 'primordial', 'signatário', 'conjuntura', 'coercitivo', 'dissolução', 'finalidade', 'itinerário', 'subjacente', 'intrínseca', 'esplêndido', 'alteridade', 'entanto', 'pecuniária', 'espontâneo', 'designação', 'transeunte', 'necessário', 'constância', 'sarcástico', 'pusilânime', 'desprovido', 'privilégio', 'idoneidade', 'verossímil', 'pernóstico', 'exacerbado', 'felicidade', 'relevância', 'divergente', 'disciplina', 'inferência', 'pernicioso', 'disseminar', 'satisfação', 'meticuloso', 'reverberar', 'esporádico', 'influência', 'militância', 'consolidar', 'retumbante', 'subversivo', 'fornicação']
repetidas = []


aleat = random.randint(0, 100)

palavra = (dic[aleat])
quant_letras = len(palavra)

print("Que os jogos comecem...")
time.sleep(2)
print("")
time.sleep(2)
print("A palavra a qual você terá que descobrir tem",quant_letras,"letras")
time.sleep(2)
print("Você terá exatamente",quant_letras,"chances para descobrir, acredito que seja o suficiente.")
time.sleep(2)
print("Boa sorte!")
time.sleep(2)
for x in range(10):

  tentativa = str(input("Tente uma letra: "))

  if repetidas.count(tentativa) == 1:
    print("Letra Repetida")
    repetidas.pop()

  repetidas.append(tentativa)

  if len(tentativa) >= 2:
    print("Olha o golpe KKKKKKK é só uma letra!")
    repetidas.pop()

  numero = any(char.isdigit() for char in tentativa)

  if bool(numero) == True:
    print("Tá achando que tá num bingo? Digite uma letra")
    repetidas.pop()

