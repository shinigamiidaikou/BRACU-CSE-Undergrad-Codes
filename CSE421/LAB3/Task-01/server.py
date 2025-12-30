import socket

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


try:
    while True:
        try:
            conn_obj, client_sock_addr = server.accept()
            print(f"[SERVER] Connected to Client {client_sock_addr}")

            connected = True
            while connected:
                upcoming_msg_len = conn_obj.recv(INIT_BUFFER_SIZE).decode(ENCODING_FORMAT)
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
                        conn_obj.send("Message Received Successfully!".encode(ENCODING_FORMAT))
                        print("[SERVER] Acknowledgment Sent!")

            conn_obj.close()

        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("\n[SERVER] Shutting down...")
    server.close()