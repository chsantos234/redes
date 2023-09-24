import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print(
        '1 - Detalhes de um(a) artista \n'
        '2 - Lista de álbums de um(a) artista\n'
        '3 - Principais de músicas de um(a) artista\n'
        '4 - Letra de alguma música'
    )

    opc = int(input('Digite a sua opção: '))
    
    # mandar o nome do artista
    if opc == 4:
        musicId = int(input('Escolha o id de alguma música: '))
        s.sendall(bytes(f'letras,{musicId}','utf-8'))
    else:
        artist = input('Informe o nome do(a) artista: ')
        if opc == 1:
            s.sendall(bytes(f'info,{artist}','utf-8'))
        elif opc == 2:
            s.sendall(bytes(f'álbuns,{artist}','utf-8'))
        elif opc == 3:
            s.sendall(bytes(f'música,{artist}','utf-8'))

    data = s.recv(4096)

print(f"Received {data.decode('utf-8')}")