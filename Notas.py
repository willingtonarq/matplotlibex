import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csvs/notas.csv")

nombres = df["nombre"]
x = range(len(nombres))

plt.bar(x, df["parcial_1"], width=0.25, label="Parcial 1", align='center')
plt.bar([i + 0.25 for i in x], df["parcial_2"], width=0.25, label="Parcial 2", align='center')
plt.bar([i + 0.50 for i in x], df["final"], width=0.25, label="Final", align='center')

plt.xticks([i + 0.25 for i in x], nombres)
plt.title("Notas por estudiante")
plt.ylabel("Nota")
plt.legend()
plt.grid(True, axis='y')
plt.ylim(0, 5)
plt.show()