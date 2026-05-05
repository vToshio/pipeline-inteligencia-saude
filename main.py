import pandas as pd

df = pd.read_csv('data/hospital_data_massive.csv', sep=';')

def main():
    global df

    # 1. Exploração inicial
    # - colunsa: id_paciente, nome, idade, oxigenacao, temperatura, pressao_arterial
    print('1. Exploração Inicial')
    print(df)
    print(df.describe())
    print("\n\nContagem de NULL:\n", df.isnull().sum(), sep='')
    print("Total de Linhas:", len(df))
    
    # 2. Remoção de Vazios
    print('\n2. Remoção de Vazios')
    print('> Remoção de IDs e Nomes vazios')
    df.dropna(subset=['id_paciente', 'nome'], inplace=True)
    print('Total de Linhas:', len(df))

    # 3. Deduplicação
    # > remoção de dados duplicados
    print("\n3. Deduplicação (remoção de duplicatas)")
    print("Dados Duplicados:", df.duplicated().sum())
    df = df.drop_duplicates()
    print('Pós deduplicação:', df.duplicated().sum())
    print('Novo total de linhas:', len(df))
    
    # 4. Integridade
    # > remoção de linhas com pressao_arterial está nula
    print('\n4. Integridade Vital (remoção de pressao_arterial nula)')
    df.dropna(subset=['pressao_arterial'], inplace=True)
    print('Novo total de linhas:', len(df))

    # 5. Inputação estratégica
    print('\n5. Inputação Estratégica')
    print('> preencher idades nulas com a mediana')
    print('> preencher oxigenação nula com 95% (valor de segurança)')
    
    mediana = df['idade'].median()               # mediana das idades
    df['idade'] = df['idade'].fillna(mediana)    # substituindo idade pela mediana
    df['oxigenacao'] = df['oxigenacao'].fillna('95%') # substituindo oxigenação nula
    print('Total de linhas:', len(df))
    print("Contagem de NULL:\n", df.isnull().sum(), sep='')
    
    # 6. Casting e Limpeza de Dados
    print('\n6. Casting e Limpeza de Dados')
    df['oxigenacao'] = df['oxigenacao'].str.replace('%', '').astype(float)
    print(df.head(5))

    # 7. Tratamento de Outliers
    print('\n7. Tratamento de Outliers')
    print('> Aplicação de um filtro para filtrar temperaturas >= 30 e <= 45')
    df = df[(df['temperatura'] >= 30) & (df['temperatura'] <= 45)]
    print('Total de linhas:', len(df))

    df.to_csv('data/output.csv')

if __name__ == "__main__":
    main()
