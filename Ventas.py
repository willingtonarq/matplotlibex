import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("csvs/ventas.csv")

meses = df["mes"]
plt.plot(meses, df["producto_a"], marker='o', label="Producto A")
plt.plot(meses, df["producto_b"], marker='s', label="Producto B")
plt.plot(meses, df["producto_c"], marker='^', label="Producto C")

plt.title("Ventas mensuales por producto")
plt.xlabel("Mes")
plt.ylabel("Unidades vendidas")
plt.grid(True)
plt.show()