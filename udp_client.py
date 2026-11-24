import socket
import time
import os

HOST = '127.0.0.1'
PORT = 65433
FILENAME = 'test_file.txt'
BUFFER_SIZE = 4096

def start_udp_client():
    if not os.path.exists(FILENAME):
        print(f"Ошибка: Файл {FILENAME} не найден.")
        return

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print(f"[UDP] Отправка файла на {HOST}:{PORT}")
        
        start_time = time.time()
        
        with open(FILENAME, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                s.sendto(data, (HOST, PORT))
        
        # Отправляем маркер окончания передачи
        s.sendto(b'END_OF_FILE', (HOST, PORT))
        
        end_time = time.time()
        print(f"[UDP] Файл отправлен.")
        print(f"[UDP] Время отправки: {end_time - start_time:.4f} сек.")

if __name__ == "__main__":
    start_udp_client()