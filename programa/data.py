# Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import os

# Nome do arquivo

caminho = "C://Users/Pc Pedro/OneDrive/Desktop/IC"

lista_arquivos = os.listdir(caminho)
CSVs = []
for i in lista_arquivos:
    if ".txt" in i:
        CSVs.append(i)
arquivo1 = CSVs[0]
arquivo2 = CSVs[1]
arquivo3 = CSVs[2]

# Função

def data(x):

    # Ajeitar o arquivo

    with open(x, "r") as arquivo:
        texto = arquivo.read()
    if (texto[0][0]) != "n":
        with open(x, "w") as arquivo:
            arquivo.write("n;Xdown;Xup\n"+texto)
            
    # Tratamento de dados

    df = pd.read_csv(x, sep = ';')

    y=0
    integral = []

    for i in range(len(df)-1):
        y = abs(df["Xdown"][i]-df["Xdown"][i+1]) + y
        integral.append(y)

    # Componentes para o gráfico

    eixo_x = []
    for i in range(len(df)-1):
        eixo_x.append(i)
        
    return(integral, eixo_x)

# Gráfico definitvo

plt.plot(data(arquivo1)[1], data(arquivo1)[0], label='dados')
plt.plot(data(arquivo2)[1], data(arquivo2)[0], label='dados')
plt.plot(data(arquivo3)[1], data(arquivo3)[0], label='dados')
plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")
plt.show()