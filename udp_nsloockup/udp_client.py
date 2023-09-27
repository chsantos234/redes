import socket
from dns import message

def send_dns_query(hostName, dnsIp):
    # Gerando socket udp do cliente
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # timeout
    udpSocket.settimeout(5)
    # porta padrão 53
    serverAddress = (dnsIp, 53)

    try:
        # Construção da mensagem a ser enviada
        query = query_constructor(hostName)
        print(query)

        # Envio da mensagem ao servidor
        udpSocket.sendto(query, serverAddress)

        # Retorno do servidor
        response,_ = udpSocket.recvfrom(2048)

        # Processamento e leitura da resposta
        response_translator(response)

    except socket.timeout:
        print("Connection timeout.")
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        udpSocket.close()

def query_constructor(hostName):
    # Formatação da query para envio 
    query = b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'
    domain = hostName.split('.')
    for part in domain:
        query += bytes([len(part)]) + part.encode('utf-8')
    query += b'\x00\x00\x01\x00\x01'

    return query

def response_translator(response):
    # tradução byte para query.message
    dns_response = response
    dns_response = message.from_wire(dns_response)
    
    print("Resposta do servidor DNS:")
    for answer in dns_response.answer:
        print(answer)
    
    first = True
    for authority in dns_response.authority:
        if first: 
            print("Servidores autoritativos:\n")
            first = False
        print(authority)

if __name__ == "__main__":
    hostName = "tiktok.com"
    dnsServeIp = "8.8.8.8"
    send_dns_query(hostName, dnsServeIp)