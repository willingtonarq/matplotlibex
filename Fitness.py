import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csvs/fitness.csv")

plt.scatter(df["edad"], df["maximo_oxigeno"], color='red')
plt.title("Consumo máximo de oxígeno vs Edad")
plt.xlabel("Edad (años)")
plt.ylabel("Consumo máximo de oxígeno (ml/kg/min)")
plt.grid(True)
plt.show()