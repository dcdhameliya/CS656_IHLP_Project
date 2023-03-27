import socket, threading

def send():
    # while True:
    msg = input('\nSelect your card >> ')
    cli_sock.send(msg.encode("utf-8"))


def receive():
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                data = data.decode("utf-8")
                print(data)
                data = eval(data)
                print("The card choosen by server is ", data['serer_card'])
                send()
        except Exception as x:
            print(x.message)
            break


if __name__ == "__main__":
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5030
    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')
    uname = input('Enter your name to start a Game:')
    cli_sock.send(uname.encode("utf-8"))

    # thread_send = threading.Thread(target=send)
    # thread_send.start()

    thread_receive = threading.Thread(target=receive)
    thread_receive.start()
