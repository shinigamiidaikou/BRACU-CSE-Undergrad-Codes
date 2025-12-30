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


def calculate_salary(hrs:str) -> str:
    try:
        hours = int(hrs)
        if hours <= 40:
            salary = hours * 200
        else:
            salary = 8000 + (hours - 40) * 300
        return f"Salary is: Tk {salary}"
    except ValueError:
        return "Invalid input for hours."


try:
    while True:
        try:
            conn_obj, client_sock_addr = server.accept()
            print(f"[SERVER] Connected to Client {client_sock_addr}")

            connected = True
            conn_obj.settimeout(5.0)
            while connected:
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
                        salary_response = calculate_salary(message)
                        conn_obj.send(salary_response.encode(ENCODING_FORMAT))
                        print("[SERVER] Salary Calculation Response Sent!")

            conn_obj.close()

        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("\n[SERVER] Keyboard Interrupt Detected. Shutting down...")
    server.close()
    print("[SERVER] Server shutdown complete.")