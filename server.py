import socket, threading, random, json


def accept_client():
    while CLIENT_COUNT[0] != 3:
        cli_sock, cli_add = ser_sock.accept()
        uname = cli_sock.recv(1024)
        uname = uname.decode("utf-8")
        CONNECTION_LIST[CLIENT_COUNT[0]]['connection'] = cli_sock
        CONNECTION_LIST[CLIENT_COUNT[0]]['name'] = uname
        CLIENT_COUNT[0] = CLIENT_COUNT[0] + 1
        # print(CONNECTION_LIST)
        print('%s is now connected' % uname)
        # print(CLIENT_COUNT)

    if CLIENT_COUNT[0] == 3:
        send_result()
        print("Server card is ", SERVER_CARDS[SERVER_CARDS_COUNTER[0]])
        for i in range(len(CONNECTION_LIST)):
            thread_client = threading.Thread(target=broadcast_usr, args=str(i))
            thread_client.start()


def send_result():
    for client in CONNECTION_LIST:
        temp_list = {
            "name": client['name'],
            "used_cards": client['used_cards'],
            "score_round": client['score_round'],
            "total_score": client['total_score'],
            "server_card": SERVER_CARDS[SERVER_CARDS_COUNTER[0]],
            "score_this_round": client['score_round'][SERVER_CARDS_COUNTER[0] - 1]
        }
        y = str(json.dumps(temp_list))
        client['connection'].send(bytes(str(y), 'utf-8'))
        print(bytes(y, 'utf-8'))


def calculate_result():
    server_card = SERVER_CARDS[SERVER_CARDS_COUNTER[0]]
    client1_card = int(CONNECTION_LIST[0]['used_cards'][-1])
    client2_card = int(CONNECTION_LIST[1]['used_cards'][-1])
    client3_card = int(CONNECTION_LIST[2]['used_cards'][-1])

    # print(client1_card)
    # print(client2_card)
    # print(client3_card)

    if client1_card >= client2_card and client1_card >= client3_card:
        CONNECTION_LIST[0]['score_round'][SERVER_CARDS_COUNTER[0]] = server_card
        # print("if 1")

    if client2_card >= client1_card and client2_card >= client3_card:
        CONNECTION_LIST[1]['score_round'][SERVER_CARDS_COUNTER[0]] = server_card
        # print("if 2")

    if client3_card >= client1_card and client3_card >= client2_card:
        CONNECTION_LIST[2]['score_round'][SERVER_CARDS_COUNTER[0]] = server_card
        # print("if 3")

    for i in range(len(CONNECTION_LIST)):
        CONNECTION_LIST[i]['total_score'] = sum(int(j) for j in CONNECTION_LIST[i]['score_round'])

    print(SERVER_CARDS[SERVER_CARDS_COUNTER[0]])
    # print(CONNECTION_LIST)

    SERVER_CARDS_COUNTER[0] = SERVER_CARDS_COUNTER[0] + 1

    send_result()


def print_card_table():
    if CARD_ACCEPT_FLAG[0] == 3:
        # print(CARD_TABLE)
        CARD_ACCEPT_FLAG[0] = 1
        calculate_result()
    else:
        CARD_ACCEPT_FLAG[0] = CARD_ACCEPT_FLAG[0] + 1


def broadcast_usr(i):
    i = int(i)
    # print(i)
    while True:
        try:
            data = CONNECTION_LIST[i]['connection'].recv(1024)
            if data:
                card = data.decode("utf-8")
                # card = card_name_from_value(card_value)
                print("{0} choose".format(CONNECTION_LIST[i]['name']), card)
                list = CONNECTION_LIST[i]['used_cards']
                list.append(int(card))
                CONNECTION_LIST[i]['used_cards'] = list
                # b_usr(cli_sock, uname, card)
                print_card_table()
        except Exception as x:
            print(x.message)
            break


# def b_usr(cs_sock, sen_name, msg):
#     for client in CONNECTION_LIST:
#         if client[1] != cs_sock:
#             client[1].send(sen_name)
#             client[1].send(msg)


if __name__ == "__main__":
    SERVER_CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    random.shuffle(SERVER_CARDS)

    CLIENT_COUNT = [0]
    SERVER_CARDS_COUNTER = [0]

    CONNECTION_LIST = [
        {
            "connection": None,
            "name": "",
            "used_cards": [],
            "score_round": [0 for element in range(13)],
            "total_score": []
        }, {
            "connection": None,
            "name": "",
            "used_cards": [],
            "score_round": [0 for element in range(13)],
            "total_score": []
        }, {
            "connection": None,
            "name": "",
            "used_cards": [],
            "score_round": [0 for element in range(13)],
            "total_score": []
        }
    ]
    CARD_TABLE = {}
    # PLAYERS = []
    CARD_ACCEPT_FLAG = [1]

    # socket
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind
    HOST = 'localhost'
    PORT = 5030
    ser_sock.bind((HOST, PORT))

    # listen
    ser_sock.listen(1)
    print('Game server started on port : ' + str(PORT))

    thread_ac = threading.Thread(target=accept_client)
    thread_ac.start()
