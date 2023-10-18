import random
import tkinter as tk

palavras = [
    "abacate",
    "amizade",
    "aniversario",
    "arco-iris",
    "aventura",
    "balao",
    "barco",
    "bicicleta",
    "brincadeira",
    "cachorro",
    "cafe",
    "carro",
    "chocolate",
    "computador",
    "coracao",
    "criatividade",
    "cultura",
    "danca",
    "doces",
    "energia",
    "escola",
    "escrita",
    "esperanca",
    "estrela",
    "familia",
    "flores",
    "felicidade",
    "fogos",
    "folhas",
    "fotografia",
    "frutas",
    "guitarra",
    "hamburguer",
    "harmonia",
    "ilusao",
    "infancia",
    "inspiracao",
    "internet",
    "inverno",
    "jardim",
    "liberdade",
    "livros",
    "lua",
    "magia",
    "natureza",
    "paz",
    "piano",
    "pintura",
    "primavera",
    "risos",
    "sabedoria",
    "saudade",
    "silencio",
    "sorriso",
    "ternura",
    "universo",
    "vento",
    "viagem",
    "amor",
    "alegria",
    "beleza",
    "amarelo",
    "vermelho",
    "azul",
    "verde",
    "roxo",
    "laranja",
    "rosa",
    "branco",
    "preto",
    "cinza",
    "dourado",
    "prateado",
    "verde-azulado",
    "marrom",
    "crescente",
    "noite",
    "estrelas",
    "luar",
    "sol",
    "ceu",
    "terra",
    "oceano",
    "rio",
    "montanha",
    "arvore",
    "flor",
    "folha",
    "raio",
    "neve",
    "chuva",
    "vento",
    "tempestade",
    "frio",
    "calor",
    "primavera",
    "verao",
    "outono",
    "inverno",
    "dia",
    "noite",
    "alvorada",
    "crepusculo",
    "amanhecer",
    "entardecer",
    "aurora",
    "ocaso",
    "horizonte",
    "manha",
    "tarde",
    "noite",
    "meio-dia",
    "meia-noite",
    "espaco",
    "tempo",
    "vida",
    "morte",
    "sonho",
    "realidade",
    "fantasia",
    "vida",
    "amizade",
    "felicidade",
    "tristeza",
    "saudade",
    "alegria",
    "paixao",
    "esperanca",
    "coragem",
    "paz",
    "guerra",
    "amor",
    "odio",
    "perdao",
    "vinganca",
    "liberdade",
    "escravidao",
    "igualdade",
    "diferenca",
    "justica",
    "injustica",
    "verdade",
    "mentira",
    "silencio",
    "palavras",
    "acao",
    "pensamento",
    "arte",
    "ciencia",
    "musica",
    "danca",
    "teatro",
    "pintura",
    "poesia",
    "literatura",
    "historia",
    "futuro",
    "passado",
    "presente",
    "caminho",
    "destino",
    "decisao",
    "escolha",
    "caminho",
    "chegada",
    "partida",
    "retorno",
    "destino",
    "jornada",
    "objetivo",
    "sonho",
    "conquista",
    "desafio",
    "superação",
    "conhecimento",
    "ignorancia",
    "curiosidade",
    "pergunta",
    "resposta",
    "busca",
    "descoberta",
    "segredo",
    "revelacao",
    "misterio",
    "sabedoria",
    "aprendizado",
    "ensinamento",
    "alma",
    "corpo",
    "mente",
    "espirito",
    "emocao",
    "sentimento",
    "pensamento",
    "intuicao",
    "racionalidade",
    "harmonia",
    "caos",
    "equilibrio",
    "desejo",
    "vontade",
    "ambicao",
    "generosidade",
    "egoismo",
    "solidariedade",
    "caridade",
    "individualidade",
    "coletividade",
    "pensamento",
    "acao",
    "reacao",
    "cause",
    "efeito",
    "yin",
    "yang",
    "equilibrio",
    "desequilibrio",
    "alegria",
    "tristeza",
    "riso",
    "lagrima",
    "inicio",
    "fim",
    "nascimento",
    "morte"
]



def escolher_palavra():
    return random.choice(palavras)

def inicializar_forca():
    forca = [
        "  +---+  ",
        "  |   |  ",
        "      |  ",
        "      |  ",
        "      |  ",
        "      |  ",
        "========="
    ]
    return forca

def exibir_forca(forca, tentativas):
    forca_atual = forca[:]

    if tentativas >= 1:
        forca_atual[2] = "  |   |  "
    if tentativas >= 2:
        forca_atual[3] = "  O   |  "
    if tentativas >= 3:
        forca_atual[4] = " /|\\  |  "
    if tentativas >= 4:
        forca_atual[3] = "|/   |  "
    if tentativas >= 5:
        forca_atual[4] = "|    |  "
    if tentativas >= 6:
        forca_atual[5] = " / \\  |  "

    canvas.delete("forca")

    for i, linha in enumerate(forca_atual):
        canvas.create_text(100, 50 + i * 20, text=linha, tags="forca")

def atualizar_interface():
    exibir_forca(forca, tentativas)
    palavra_oculta_label.config(text="Palavra: " + " ".join(palavra_oculta))
    letras_erradas_label.config(text="Letras erradas: " + ", ".join(letras_erradas))

    if "_" not in palavra_oculta:
        resultado_label.config(text="Parabéns! Você ganhou! A palavra é: " + palavra)
    elif tentativas >= 6:
        resultado_label.config(text="Você perdeu! A palavra era: " + palavra)

def verificar_letra(event=None):
    global tentativas
    letra = letra_entry.get().lower()

    if len(letra) != 1 or not letra.isalpha():
        resultado_label.config(text="Por favor, digite uma única letra válida.")
    else:
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas += 1

    atualizar_interface()

janela = tk.Tk()
janela.title("Jogo da Forca")
janela.configure(bg="royalblue3")

canvas = tk.Canvas(janela, width=200, height=200)
canvas.pack()

forca = inicializar_forca()
palavra = escolher_palavra()
palavra_oculta = ["_"] * len(palavra)
tentativas = 0
letras_erradas = []

palavra_oculta_label = tk.Label(janela, text="Palavra: ")
palavra_oculta_label.pack()


letras_erradas_label = tk.Label(janela, text="Letras erradas: ")
letras_erradas_label.pack()


letra_entry = tk.Entry(janela)
letra_entry.pack()


letra_entry.bind("<Return>", verificar_letra)


verificar_letra_button = tk.Button(janela, text="Verificar Letra", command=verificar_letra)
verificar_letra_button.pack()


resultado_label = tk.Label(janela, text="")
resultado_label.pack()


atualizar_interface()


janela.mainloop()
