"""Dashboard de Livros: app Streamlit."""

import streamlit as st
from dados import ler_livros


def calcular_preco_medio(livros):
    total = 0

    for livro in livros:
        preco = float(livro["preco"].replace("£", ""))
        total += preco

    return total / len(livros)


def contar_cinco_estrelas(livros):
    quantidade = 0

    for livro in livros:
        if livro["nota"] == "Five":
            quantidade += 1

    return quantidade


def encontrar_livro_mais_caro(livros):
    mais_caro = livros[0]

    for livro in livros:
        preco_atual = float(livro["preco"].replace("£", ""))
        preco_mais_caro = float(mais_caro["preco"].replace("£", ""))

        if preco_atual > preco_mais_caro:
            mais_caro = livro

    return mais_caro


st.title("📚 Dashboard de Livros")

livros = ler_livros()

preco_medio = calcular_preco_medio(livros)
cinco_estrelas = contar_cinco_estrelas(livros)
livro_mais_caro = encontrar_livro_mais_caro(livros)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de livros", len(livros))

with col2:
    st.metric("Preço médio", f"£{preco_medio:.2f}")

with col3:
    st.metric("Livros com 5 estrelas", cinco_estrelas)

with col4:
    st.metric("Livro mais caro", livro_mais_caro["preco"])
    st.caption(livro_mais_caro["titulo"])

st.dataframe(livros)