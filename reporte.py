import pandas as pd
from fpdf import FPDF

# Cargar los datos procesados
df = pd.read_csv("processed_stock_data.csv")

# Calcular estadísticas básicas
mean_price = df["price"].mean()
max_price = df["price"].max()
min_price = df["price"].min()

# Crear documento PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Título
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, "Reporte de Análisis de Datos de Acciones", ln=True, align="C")
pdf.ln(10)

# Sección de Estadísticas
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Precio promedio: {mean_price:.2f}", ln=True)
pdf.cell(200, 10, f"Precio máximo: {max_price:.2f}", ln=True)
pdf.cell(200, 10, f"Precio mínimo: {min_price:.2f}", ln=True)
pdf.ln(10)

# Agregar imagen de la gráfica generada
pdf.image("grafico_stock_data.png", x=10, y=None, w=180)

# Guardar PDF
pdf.output("reporte_final.pdf")

print("✅ Reporte generado: reporte_final.pdf")
