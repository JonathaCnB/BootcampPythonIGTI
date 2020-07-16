def selecaoPalavra():
    from random import choice
    forca = ["Caneca", "Celular", "Clube", "Copo", "Doce", "Elefante", "Escola", "Estojo", "Faca", "Foto", "Garfo", "Geleia",
              "Girafa", "Janela", "Limonada", "Mae", "Meia", "Noite", "Oculos", "onibus", "Ovo", "Pai", "Pao", "Parque",
              "Passarinho", "Peixe", "Pijama", "Rato", "Umbigo", "Amarelo", "Amiga", "Amor", "Ave", "Aviao", "Avo", "Balao",
              "Bebe", "Bolo", "Branco", "Cama"]
    selecao = choice(forca)
    return str(selecao.upper())


def verificaString(t):
    valido = False
    while not valido:
        entrada = str(input(t))
        if entrada.isalpha():
            valido = True
            return str(entrada).strip().upper()
        else:
            print(f'\033[0;31mDigite um caracter valido!\033[m')

