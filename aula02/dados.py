"""Leitura dos arquivos CSV do projeto."""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros():
    """Lê o CSV de livros e devolve uma lista de dicionários.

    Os valores vêm do jeito que estão no arquivo, ou seja, como texto:
    {"titulo": "Sharp Objects", "preco": "£47.82", "nota": "Four", ...}
    """
    livros = []

    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                livros.append(linha)

    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")

    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return livros


def calcular_preco_medio(livros):
    """Soma os preços de todos os livros e divide pelo total."""

    soma = 0

    for livro in livros:
        soma += livro["preco"]

    preco_medio = soma / len(livros)

    return preco_medio


def contar_cinco_estrelas(livros):
    """Conta quantos livros têm a nota máxima."""

    contador = 0

    for livro in livros:
        if livro["nota"] == 5:
            contador += 1

    return contador


def encontrar_mais_caro(livros):
    """Devolve o livro de maior preço."""

    mais_caro = livros[0]

    for livro in livros:
        if livro["preco"] > mais_caro["preco"]:
            mais_caro = livro

    return mais_caro


def converter_preco(preco):
    return float(preco.replace("£", ""))


def converter_nota(nota):
    if nota == "One":
        return 1
    elif nota == "Two":
        return 2
    elif nota == "Three":
        return 3
    elif nota == "Four":
        return 4
    elif nota == "Five":
        return 5
    else:
        return 0


def preparar_livros(linhas):
    livros = []

    for linha in linhas:
        livro = {
            "titulo": linha["titulo"],
            "preco": converter_preco(linha["preco"]),
            "nota": converter_nota(linha["nota"]),
            "categoria": linha["categoria"],
        }

        livros.append(livro)

    return livros


def carregar_livros():
    return preparar_livros(ler_livros())


if __name__ == "__main__":
    livros = carregar_livros()

    print(f"{len(livros)} livros carregados")
    print("Primeiro livro:", livros[0])