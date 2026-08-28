import streamlit as st

st.title('Elementos interativos de Layout')
st.sidebar.header('Opções da aplicação')
nome = st.sidebar.text_input('Nome')
st.sidebar.write(f'Olá, {nome}')

colunas = st.columns(2)

with colunas[0]:
    st.header('Interações simples')
    if st.button('Me aperte'):
        st.success('Você clicou no botão!')
        st.balloons()
    else:
        st.error('Você ainda não apertou...')

    valor_slider = st.slider(
        label='Selecione um valor', 
        min_value=0, 
        max_value=100, 
        value=50
    )
    st.write(f'O valor selecionado no slider é: {valor_slider}')

with colunas[1]:
    st.header('Informações e Imagens')
    st.info('Esta é uma mensagem informativa!')

    st.image(
        'https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png', 
        caption='Logo do Streamlit', 
        use_container_width=True
    )