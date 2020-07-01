import pandas as pd


#notas = pd.Series([2,7,5,10,6], index=["Wilfred", "Abbie", "Harry", "Julia", "Carrie"])

#print(notas)
#print(notas.index[0])



df = pd.read_csv("FurtosAtualizada1.csv",sep =";", encoding='ISO-8859-1')

#print(df.info())
#print(df.columns)

#maiorBairro = df[["Bairro"].value_counts().head(1)]
maior = df["Bairro"].value_counts().head(10)
maximoBairro = maior.index[0]
x = maior.get_value(0,1)

# print(maior)
# print("------------------------------")
# print (df["Bairro"].value_counts().head(10))
# print (df["Bairro"].value_counts().tail())
# print("--------------------------------------------")

# print("--------------------------------------")
# print (df["DiaOcorrencia"].value_counts().head(10))
dia =df["DiaOcorrencia"].value_counts().head(10)
yy = dia.index[0]
# print("--------------------------------------")
# print (df["TurnoOcorrencia"].value_counts().head())
turno = df["TurnoOcorrencia"].value_counts().head()
teste= turno.get_value(3,1)
# print(teste)
# print('---------------------------------')
zz = turno.index[0]


def week(i):
        switcher={
                1:'Domingo',
                2:'Segunda',
                3:'Terça',
                4:'Quarta',
                5:'Quinta',
                6:'Sexta',
                7:'Sabado'
             }
        return switcher.get(i,'Invalido')
    
    
def turno(i):
        switcher={
                1:'Manha',
                2:'Tarde',
                3:'Noite'
             }
        return switcher.get(i,'Invalido')
semanal = week(yy)
turn = turno(zz)
#print(semanal)