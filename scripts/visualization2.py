import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos procesados
df = pd.read_csv("processed_stock_data.csv")

# Graficar precios de la acción
plt.figure(figsize=(10,5))
plt.plot(df["time"], df["price"], marker="o", linestyle="-", color="b")
plt.xlabel("Tiempo")
plt.ylabel("Precio")
plt.title("Evolución del Precio de la Acción")
plt.xticks(rotation=45)
plt.show()
