import dask.dataframe as dd
import pandas as pd

# Leer el archivo CSV con Dask
df = dd.read_csv("processed_stock_data.csv")

# Convertir la columna 'time' a formato de fecha (por si no lo está)
df['time'] = dd.to_datetime(df['time'])

# Asegurar que la columna 'price' sea numérica
df['price'] = df['price'].astype(float)

# Filtrar los datos para eliminar precios menores a 0 (si existieran)
df = df[df['price'] > 0]

# Calcular estadísticas clave de los precios
mean_price = df['price'].mean().compute()
max_price = df['price'].max().compute()
min_price = df['price'].min().compute()

# Agrupar por fecha y calcular la media por día
df_grouped = df.groupby(df['time'].dt.date)['price'].mean().compute()

# Guardar los datos procesados en un nuevo CSV
df_grouped.to_csv("processed_stock_data_summary.csv", index=True)

# Mostrar resultados
print(f"📊 Estadísticas Generales:")
print(f"🔹 Precio Promedio: {mean_price:.2f}")
print(f"🔹 Precio Máximo: {max_price:.2f}")
print(f"🔹 Precio Mínimo: {min_price:.2f}")

print("✅ Datos procesados y guardados en 'processed_stock_data_summary.csv'.")
