import socket, threading
import tkinter as tk
from PIL import Image, ImageTk

r = tk.Tk()
r.title('A Game of Strategy')
r.geometry("1000x1000")

serverCard = tk.Label(r, text = "Server Card:").place(x = 200,y = 150)

def card_name_from_value(card_value):
    card_value = int(card_value)

    if card_value == 1:
        return 'A'
    elif card_value == 11:
        return "J"
    elif card_value == 12:
        return "Q"
    elif card_value == 13:
        return "K"
    else:
        return card_value


def card_value_from_name(card_value):
    if card_value == 'A' or card_value == 'a':
        return 1
    elif card_value == 'J' or card_value == 'j':
        return 11
    elif card_value == 'Q' or card_value == 'q':
        return 12
    elif card_value == 'K' or card_value == 'k':
        return 13
    else:
        return int(card_value)


def send():
    print('send')
    while True:
        print('aa')

        def setmsg(e):
            print('heyyyyyyyy')
            print(e)
            # msg = card_value_from_name(button.image.name)

            # if msg < 1 or 13 < msg:
            #     print("Invalid card Please choose valid card...")
            #     continue
            # elif msg in CARD_LIST:
            #     print("You already used this card please choose another one....")
            #     continue
            # else:
            #     CARD_LIST.append(msg)
            #     break
            
            # print(msg)


        L1=tk.Label(text='Select your card')
        L1.place(x = 30,y = 200)
        
        image1 = ImageTk.PhotoImage(Image.open("C_2.png").resize((100,200), Image.ANTIALIAS))

        button = tk.Button(r, image=image1,command=setmsg,borderwidth=0)
        button.place(x = 30,y = 200)
        
    # cli_sock.send(str(msg).encode("utf-8"))


def receive():
    print('receive')
    while True:
        try:
            data = cli_sock.recv(1024)
            print('data')
            print(data)
            if data:
                data = data.decode("utf-8")
                # print(data)
                data = eval(data)

                if len(data['used_cards']) != 0:
                    print("You get ", data['score_this_round'], " in this round")
                    print("Your total score is ", data['total_score'])

                print("\n\n\n\nThe card choosen by server is ", card_name_from_value(data['server_card']))
                send()
        except Exception as x:
            print(x.message)
            break


if __name__ == "__main__":
    CARD_LIST = []
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5030
    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')

    # thread_send = threading.Thread(target=send)
    # thread_send.start()

    
    # r.configure(bg='white')

    

    def connect_uname():
        print(nameinp.get())
        cli_sock.send(nameinp.get().encode("utf-8"))

    titleLabel = tk.Label(r, text="A Game of Strategy! Let's Play!")
    ipLabel = tk.Label(r, text = "Enter your name to start a Game:").place(x = 30,y = 50)

    nameinp = tk.StringVar()
    unameText = tk.Entry(r,textvar=nameinp,width = 20).place(x = 400, y = 50)

    startButton = tk.Button(r, text = "Play Game",command = connect_uname).place(x = 30, y = 100)

    scoreLabel = tk.Label(r, text = "Your Current Score:").place(x = 30,y = 150)
    scoreDisplayLabel = tk.Label(r, text = "0").place(x = 180,y = 150)


    thread_receive = threading.Thread(target=receive)
    thread_receive.start()
    
    r.mainloop()