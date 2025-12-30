import socket

INIT_BUFFER_SIZE = 16
ENCODING_FORMAT = 'utf-8'
SERVER_NAME = socket.gethostname()
SERVER_IP = socket.gethostbyname(SERVER_NAME)
SERVER_PORT = 5050

server_socket_address = (SERVER_IP, SERVER_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)


def send_msg_to_server(msg:str) -> None:
    message = msg.encode(ENCODING_FORMAT)
    msg_len = str(len(message)).encode(ENCODING_FORMAT)
    msg_len += b" "*(INIT_BUFFER_SIZE-len(msg_len))

    client.send(msg_len)
    client.send(message)

    sent_from_server = client.recv(1024).decode(ENCODING_FORMAT)
    print(f"[Server Response] {sent_from_server}")


send_msg_to_server(f"My device name is {SERVER_NAME} and my IP address is {SERVER_IP}.")
send_msg_to_server("Disconnect")
client.close()