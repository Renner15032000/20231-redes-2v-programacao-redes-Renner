import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('10.25.1.31', 65003)

    while True:
        message = input('Digite uma mensagem (quit para encerrar): ')

        data = message.encode('utf-8')
        client_socket.sendto(data, server_address)

        if message == 'quit':
            break


    client_socket.close()


if __name__ == '__main__':
    main()