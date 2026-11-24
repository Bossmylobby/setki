import socket
import time
import os

HOST = '127.0.0.1'
PORT = 65432
FILENAME = 'test_file.txt' # Файл, который будем отправлять

def start_tcp_client():
    if not os.path.exists(FILENAME):
        print(f"Ошибка: Файл {FILENAME} не найден. Создайте его.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[TCP] Подключение к серверу {HOST}:{PORT}")
        
        start_time = time.time()
        
        with open(FILENAME, 'rb') as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                s.sendall(data)
                
        end_time = time.time()
        print(f"[TCP] Файл отправлен.")
        print(f"[TCP] Время отправки: {end_time - start_time:.4f} сек.")

if __name__ == "__main__":
    start_tcp_client()