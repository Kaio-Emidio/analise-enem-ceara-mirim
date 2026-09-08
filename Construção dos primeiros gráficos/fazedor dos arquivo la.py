import pandas as pd

tabela_int = pd.read_csv('MICRODADOS_ENEM_2024.csv', encoding='latin-1', delimiter=';')

colunas_de_interesse = ['CO_MUNICIPIO_PROVA','NU_NOTA_CN','NU_NOTA_CH','NU_NOTA_LC','NU_NOTA_MT','NU_NOTA_REDACAO']
novos_nomes = {
    'NU_NOTA_CN': 'Ciências da Natureza',
    'NU_NOTA_CH': 'Ciências Humanas',
    'NU_NOTA_LC': 'Linguagens e Códigos',
    'NU_NOTA_MT': 'Matemática',
    'NU_NOTA_REDACAO': 'Redação',
    'CO_MUNICIPIO_PROVA': 'Município da Prova'
}

tabela_filtrada = tabela_int[colunas_de_interesse]

tabela_filtrada.rename(inplace=True, columns=novos_nomes)

print(tabela_filtrada.columns.tolist())

tabela_filtrada.to_csv('dados.csv', sep=';', index=False, encoding='utf-8-sig')