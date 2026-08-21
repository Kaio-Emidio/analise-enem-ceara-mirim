import streamlit as st

st.title("Minha primeira aplicação com Streamlit!")
st.header("Hello, World!")
st.subheader("Vamos explorar essa ferramenta incrível!")
st.write("Este é um texto simples utilizando o st.write :D")
st.markdown('''
    Este é um exemplo de markdown no streamlit:
    Podemos usar o **Negrito**, *itálico* e até mesmo **Listas:**
    * Item 1
    * Item 2
''')
st.text('Este é um texto puro, sem formatação!')