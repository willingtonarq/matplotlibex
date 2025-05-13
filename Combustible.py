import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csvs/combustible.csv")

plt.plot(df["distancia_km"], df["litros_usados"], marker='o', color='green')
plt.title("Consumo de combustible")
plt.xlabel("Distancia recorrida (km)")
plt.ylabel("Litros usados")
plt.grid(True)
plt.show()
