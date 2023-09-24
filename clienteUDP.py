import socket

# Endereço e porta do servidor UDP
server_ip = '127.0.0.1'
server_port = 12345

# Crie um socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    artist_name = "info,taylor swift"

    if artist_name.lower() == 'sair':
        break


    udp_socket.sendto(artist_name.encode("utf-8"), (server_ip, server_port))

    response, server_address = udp_socket.recvfrom(1024)
    print(response.decode("utf-8"))


udp_socket.close()
