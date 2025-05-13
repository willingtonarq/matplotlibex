import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csvs/clima.csv")

plt.plot(df["dia"], df["temperatura"], marker='o', label="Temperatura (°C)")
plt.bar(df["dia"], df["lluvia"], alpha=0.3, label="Lluvia (mm)", color="blue")

plt.title("Clima diario")
plt.xlabel("Día")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)
plt.show()