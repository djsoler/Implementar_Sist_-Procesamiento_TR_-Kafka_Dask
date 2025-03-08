import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos procesados
df = pd.read_csv("processed_stock_data.csv")

# Convertir la columna 'time' a formato de fecha
df['time'] = pd.to_datetime(df['time'])

# Ordenar los datos por tiempo (por si hay desorden)
df = df.sort_values(by='time')

# Generar la gráfica
plt.figure(figsize=(10, 5))
plt.plot(df['time'], df['price'], marker='o', linestyle='-', color='b', label='Precio de la acción')

# Personalización del gráfico
plt.xlabel("Tiempo")
plt.ylabel("Precio de la acción")
plt.title("Evolución del Precio de la Acción en Tiempo Real")
plt.legend()
plt.xticks(rotation=45)
plt.grid()

# Guardar la imagen
plt.savefig("grafico_stock_data.png")

# Mostrar la gráfica
plt.show()
