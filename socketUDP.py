import socket
import json
from extractor.genius_extractor import extractor

# Endereço e porta do servidor UDP
server_ip = '127.0.0.1'
server_port = 12345

# Crie um socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((server_ip, server_port))

print(f"O servidor UDP está ouvindo em {server_ip}:{server_port}")

while True:
    data, client_address = udp_socket.recvfrom(1024)

    try:
        data_str = data.decode("utf-8")

        api_response = extractor(data_str)

        udp_socket.sendto(json.dumps(api_response).encode("utf-8"), client_address)

    except UnicodeDecodeError:
        udp_socket.sendto("Erro: Não foi possível decodificar os dados.".encode("utf-8"), client_address)
