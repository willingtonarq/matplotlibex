import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv("csvs/datos.csv")

# Acceder a las columnas
x = df["tiempo"]
y = df["temperatura"]

# Graficar
plt.plot(x, y, marker='o')
plt.title("Temperatura en el tiempo")
plt.xlabel("Tiempo (horas)")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.show()