import socket
import threading

INIT_BUFFER_SIZE = 16
ENCODING_FORMAT = 'utf-8'
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
SERVER_PORT = 5050

server_socket_address = (SERVER_IP, SERVER_PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)

server.listen()
server.settimeout(3.0)
print("[SERVER] listening...\n")


def count_vowels(message:str) -> str:
    vowels = "aeiouAEIOU"
    count = 0
    for char in message:
        if char in vowels:
            count += 1
    if count == 0:
        return "Not enough vowels"
    elif count <= 2:
        return "Enough vowels I guess"
    else:
        return "Too many vowels"


def handle_clients(conn_obj:socket.socket, client_sock_addr:tuple[str, int], shutdown_event:threading.Event) -> None:
    print(f"[SERVER] Connected to Client {client_sock_addr}")

    connected = True
    conn_obj.settimeout(5.0)
    while connected and not shutdown_event.is_set():
        try:
            upcoming_msg_len = conn_obj.recv(INIT_BUFFER_SIZE).decode(ENCODING_FORMAT)
        except socket.timeout:
            continue
        print(f"[CLIENT {client_sock_addr[0]}:{client_sock_addr[1]}]", upcoming_msg_len)

        if upcoming_msg_len:
            print(f"[SERVER] Upcoming message length: {int(upcoming_msg_len)} bytes. (Buffer Adjusted)")
            message = conn_obj.recv(int(upcoming_msg_len)).decode(ENCODING_FORMAT)
            if message == "Disconnect":
                connected = False
                conn_obj.send("Goodbye".encode(ENCODING_FORMAT))
                print("[SERVER] Client Terminated Connection:", client_sock_addr)
            else:
                print(f"[CLIENT {client_sock_addr[0]}:{client_sock_addr[1]}] {message}")
                vowel_response = count_vowels(message)
                conn_obj.send(vowel_response.encode(ENCODING_FORMAT))
                print("[SERVER] Vowel Count Response Sent!")

    conn_obj.close()


shutdown_event = threading.Event()
active_threads:list[threading.Thread] = []

try:
    while True:
        try:
            conn_obj, client_sock_addr = server.accept()
            client_thread = threading.Thread(target=handle_clients, args=(conn_obj, client_sock_addr, shutdown_event))
            active_threads.append(client_thread)
            client_thread.start()

        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("\n[SERVER] Keyboard Interrupt Detected. Shutting down...")
    shutdown_event.set()

    # Wait for all threads to finish gracefully
    print("[SERVER] Waiting for client threads to finish...")
    for thread in active_threads:
        thread.join(timeout=60.0)

    server.close()
    print("[SERVER] Server shutdown complete.")
