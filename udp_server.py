import socket
import time

HOST = '127.0.0.1'
PORT = 65433
FILENAME = 'received_udp.txt'
BUFFER_SIZE = 4096

def start_udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[UDP] Сервер запущен на {HOST}:{PORT}. Ожидание данных...")
        
        total_bytes = 0
        start_time = None
        
        with open(FILENAME, 'wb') as f:
            while True:
                data, addr = s.recvfrom(BUFFER_SIZE)
                
                if start_time is None:
                    start_time = time.time() # Начинаем замер при получении первого пакета
                
                if data == b'END_OF_FILE':
                    break
                
                f.write(data)
                total_bytes += len(data)
        
        end_time = time.time()
        print(f"[UDP] Файл успешно получен. Размер: {total_bytes} байт.")
        print(f"[UDP] Время передачи: {end_time - start_time:.4f} сек.")

if __name__ == "__main__":
    start_udp_server()