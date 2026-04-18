import pandas as pd

df = pd.read_excel('data/Worked dataset- DataSense.xlsx')

print(df.head(10))


publicoalvo = df[df['Purchased Bike'] == "Yes"]


perfil = {
    "idade_media": publicoalvo["Age"].mean(),
    "renda_media": publicoalvo["Income"].mean(),
    "regiao_top": publicoalvo["Region"].mode()[0],
    "distancia_top": publicoalvo["Commute Distance"].mode()[0],
    "educacao_top": publicoalvo["Education"].mode()[0],
}

print(perfil)

print(df["Region"].value_counts())

not_buy = df[df['Purchased Bike'] == "No"]

comparacao = {
    "idade_comprou": publicoalvo["Age"].mean(),
    "idade_nao": not_buy["Age"].mean(),
    "renda_comprou": publicoalvo["Income"].mean(),
    "renda_nao": not_buy["Income"].mean(),
}
print(comparacao)