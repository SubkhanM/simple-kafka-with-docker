import time
import random
from kafka import KafkaProducer
import json

# Koneksi ke Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def generate_sensor_data(sensor_id):
    # Mensimulasikan suhu antara 60°C - 100°C sebagai integer
    suhu = random.randint(60, 100)
    return {'sensor_id': sensor_id, 'suhu': suhu}

sensor_ids = ['S1', 'S2', 'S3']  # Tiga sensor

try:
    while True:
        for sensor_id in sensor_ids:
            data = generate_sensor_data(sensor_id)
            producer.send('sensor-suhu', data)
            print(f"Mengirim data: {data['sensor_id']} - {data['suhu']}°C")  # Menampilkan dengan "°C"
        time.sleep(1)
except KeyboardInterrupt:
    producer.close()
    print("Producer stopped.")
