"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

def montar_tabela(livros):
    """Devolve uma tabela com os livros."""

    tabela = []

    for livro in livros:
        linha = {
            "Título": livro["titulo"],
            "Preço": f"£{livro['preco']:.2f}",
            "Nota": livro["nota"] * "⭐",
            "Categoria": livro["categoria"],
            "Faixa": classificar_preco(livro["preco"])
        }

        tabela.append(linha)

    return tabela

def conta_por_faixa_dict(livros):
    contagem = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])
        if faixa in contagem:
            contagem[faixa] += 1
        else:
            contagem[faixa] = 1
    return contagem

def classificar_preco(preco):
    """Devolve a classificação do preço."""

    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Médio"
    else:
        return "Caro"

def contar_por_faixa(livros):
    conta_caros = 0
    conta_medios = 0
    conta_baratos = 0
    for livro in livros:
        if classificar_preco(livro["preco"]) == "Caro":
            conta_caros += 1
        elif classificar_preco(livro["preco"]) == "Médio":
            conta_medios += 1
        else:
            conta_baratos += 1
    return conta_caros, conta_medios, conta_baratos

def main():
    st.set_page_config(
        page_title="Dashboard de Livros",
        page_icon="📚",
        layout="wide"
    )

    st.title("📚 Dashboard de Livros")

    livros = dados.carregar_livros()
    tabela = montar_tabela(livros)

    col1, col2, col3, col4 = st.columns(4)

    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro", f"£{mais_caro['preco']:.2f}")
    col4.caption(mais_caro["titulo"])

    st.dataframe(tabela)


if __name__ == "__main__":
    main()