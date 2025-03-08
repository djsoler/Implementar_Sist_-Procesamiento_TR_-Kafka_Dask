from kafka import KafkaProducer
import json
import time
from alpha_vantage.timeseries import TimeSeries

# Configuración de Alpha Vantage
API_KEY = "TU_API_KEY"  # Sustituye con tu clave real
SYMBOL = "AAPL"
INTERVAL = "1min"

# Configuración de Kafka
TOPIC = "stock_data"
KAFKA_SERVER = "localhost:9092"

# Inicializar el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Función para obtener datos
def fetch_stock_data():
    ts = TimeSeries(key=API_KEY, output_format="json")
    data, meta = ts.get_intraday(symbol=SYMBOL, interval=INTERVAL, outputsize="compact")
    
    latest_time = list(data.keys())[0]
    stock_info = {"time": latest_time, "price": data[latest_time]["1. open"]}
    
    return stock_info

# Enviar datos a Kafka cada 10 segundos
while True:
    stock_data = fetch_stock_data()
    producer.send(TOPIC, stock_data)
    print(f"Datos enviados: {stock_data}")
    time.sleep(10)
