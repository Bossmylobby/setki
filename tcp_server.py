import socket
import time

HOST = '127.0.0.1'
PORT = 65432
FILENAME = 'received_tcp.txt'

def start_tcp_server():
    # Создаем TCP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[TCP] Сервер запущен на {HOST}:{PORT}. Ожидание подключения...")
        
        conn, addr = s.accept()
        with conn:
            print(f"[TCP] Подключен клиент: {addr}")
            
            # Замер времени начинается с получением первого байта
            start_time = time.time()
            total_bytes = 0
            
            with open(FILENAME, 'wb') as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)
                    total_bytes += len(data)
            
            end_time = time.time()
            print(f"[TCP] Файл успешно получен. Размер: {total_bytes} байт.")
            print(f"[TCP] Время передачи: {end_time - start_time:.4f} сек.")

if __name__ == "__main__":
    start_tcp_server()