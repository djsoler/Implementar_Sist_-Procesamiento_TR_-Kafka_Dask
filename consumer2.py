from kafka import KafkaConsumer
import json
import pandas as pd

# Configuración de Kafka
TOPIC = "stock_data"
KAFKA_SERVER = "localhost:9092"

# Inicializar el consumidor de Kafka
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='stock-data-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🟢 Esperando datos...")

# Lista para almacenar los datos recibidos
data_list = []

for message in consumer:
    data = message.value  # Obtiene el valor del mensaje recibido
    print(f"Datos recibidos: {data}")

    # Agregar el mensaje a la lista
    data_list.append(data)

    # Guardar los datos en un archivo CSV correctamente
    df = pd.DataFrame(data_list, columns=["time", "price"])
    df.to_csv("processed_stock_data.csv", index=False)
