import socket, threading
from tkinter import *
from PIL import Image, ImageTk

# socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
HOST = 'localhost'
PORT = 5036
cli_sock.connect((HOST, PORT))
cli_sock.send("Client 2".encode("utf-8"))

window = Tk("Client 2")
window.geometry("1200x800")
window.configure(background="#008000")
window.iconbitmap(r'pictures/icon.ico')
info_menu = Menu(window)

text = Label(window, text="Score: 0", bg="green")
text.place(x=0, y=0)


def clear_center_frame():
    for widgets in frame_cards_middle.winfo_children():
        widgets.destroy()


def set_winner_name(msg):
    winner_message = Label(window, text=msg, bg="green")
    winner_message.place(x=600, y=350)


def set_score(score):
    text.configure(text="Score: " + str(score))


def unused_resize_cards(card):
    entry_card = Image.open(card)
    resized_image = entry_card.resize((65, 93))
    global final_card
    final_card = ImageTk.PhotoImage(resized_image)
    return final_card


def center_resize_card(card):
    global final_card
    entry_card = Image.open(card)
    resized_image = entry_card.resize((160, 230))
    final_card = ImageTk.PhotoImage(resized_image)
    return final_card


FLAG = [True]


def cards_in_the_middle(card_number):
    global photos_cards_player
    card = center_resize_card(photos_cards_player[card_number])
    panel_0 = Label(frame_cards_middle, image=card, bg="green")
    panel_0.grid(row=0, column=0)
    msg = card_number + 1
    cli_sock.send(str(msg).encode("utf-8"))

    if FLAG[0] == False:
        for child in frame_cards_player.winfo_children():
            child.configure(state='disable')
        FLAG[0] = True


def server_cards_in_the_middle(card_number):
    resized_card = "images/S_" + str(card_number) + ".png"
    card = unused_resize_cards(resized_card)
    panel_1 = Label(frame_cards_computer, image=card, bg="green")
    panel_1.grid(row=0, column=0)

    if FLAG[0]:
        for child in frame_cards_player.winfo_children():
            child.configure(state='normal')
        FLAG[0] = False


def receive():
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                data = data.decode("utf-8")
                # print(data)
                data = eval(data)

                if len(data['used_cards']) != 0:
                    print("You get ", data['score_this_round'], " in this round")
                    print("Your total score is ", data['total_score'])
                    set_score(data['total_score'])

                if "winner_name" in data.keys():
                    clear_center_frame()

                    if data['name'] in data['winner_name']:
                        set_winner_name("Congrates you win the game...")
                    else:
                        # print("you are not the winner")s
                        set_winner_name("Winner is " + ", ".join(data['winner_name']))
                    break

                else:
                    print("\n\n\n\nThe card choosen by server is ", data['server_card'])
                    server_cards_in_the_middle(int(data['server_card']))
        except Exception as x:
            print(x.message)
            break


thread_receive = threading.Thread(target=receive)
thread_receive.start()

window.config(menu=info_menu)
info_game = Menu(info_menu, tearoff=0)
info_menu.add_cascade(label="Info", menu=info_game)
# info_game.add_command(label="About the game", command=about_game)
info_game.add_separator()
# info_game.add_command(label="How to play?", command=how_to_play)

frame_cards_computer = Frame(window, bg="green")
frame_cards_computer.pack(side=TOP)

frame_cards_player = Frame(window, bg="green")
frame_cards_player.pack(side=BOTTOM)

frame_cards_middle = Frame(window, bg='green')
frame_cards_middle.place(relx=0.5, rely=0.5,  anchor=CENTER)


window.config(menu=info_menu)
frame_victory = Frame(window, bg='green')

photos_cards_player = []
unused_resize_cards_list = []

for i in range(13):
    resized_card = "images/H_" + str(i + 1) + ".png"
    photos_cards_player.append(resized_card)

for i in photos_cards_player:
    unused_resize_cards_list.append(unused_resize_cards(i))

card_button = []

image_button_1 = Button(frame_cards_player, image=(unused_resize_cards_list[0]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_1.grid_forget(), cards_in_the_middle(0)],
                        state=NORMAL)
image_button_1.grid(row=0, column=1)

image_button_2 = Button(frame_cards_player, image=(unused_resize_cards_list[1]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_2.grid_forget(), cards_in_the_middle(1)],
                        state=NORMAL)
image_button_2.grid(row=0, column=2)

image_button_3 = Button(frame_cards_player, image=(unused_resize_cards_list[2]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_3.grid_forget(), cards_in_the_middle(2)],
                        state=NORMAL)
image_button_3.grid(row=0, column=3)

image_button_4 = Button(frame_cards_player, image=(unused_resize_cards_list[3]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_4.grid_forget(), cards_in_the_middle(3)],
                        state=NORMAL)
image_button_4.grid(row=0, column=4)

image_button_5 = Button(frame_cards_player, image=(unused_resize_cards_list[4]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_5.grid_forget(), cards_in_the_middle(4)],
                        state=NORMAL)
image_button_5.grid(row=0, column=5)

image_button_6 = Button(frame_cards_player, image=(unused_resize_cards_list[5]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_6.grid_forget(), cards_in_the_middle(5)],
                        state=NORMAL)
image_button_6.grid(row=0, column=6)

image_button_7 = Button(frame_cards_player, image=(unused_resize_cards_list[6]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_7.grid_forget(), cards_in_the_middle(6)],
                        state=NORMAL)
image_button_7.grid(row=0, column=7)

image_button_8 = Button(frame_cards_player, image=(unused_resize_cards_list[7]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_8.grid_forget(), cards_in_the_middle(7)],
                        state=NORMAL)
image_button_8.grid(row=0, column=8)

image_button_9 = Button(frame_cards_player, image=(unused_resize_cards_list[8]), bg="green", bd=0,
                        fg="green",
                        command=lambda: [image_button_9.grid_forget(), cards_in_the_middle(8)],
                        state=NORMAL)
image_button_9.grid(row=0, column=9)

image_button_10 = Button(frame_cards_player, image=(unused_resize_cards_list[9]), bg="green", bd=0,
                         fg="green",
                         command=lambda: [image_button_10.grid_forget(), cards_in_the_middle(9)],
                         state=NORMAL)
image_button_10.grid(row=0, column=10)

image_button_11 = Button(frame_cards_player, image=(unused_resize_cards_list[10]), bg="green", bd=0,
                         fg="green",
                         command=lambda: [image_button_11.grid_forget(), cards_in_the_middle(10)],
                         state=NORMAL)
image_button_11.grid(row=0, column=11)

image_button_12 = Button(frame_cards_player, image=(unused_resize_cards_list[11]), bg="green", bd=0,
                         fg="green",
                         command=lambda: [image_button_12.grid_forget(), cards_in_the_middle(11)],
                         state=NORMAL)
image_button_12.grid(row=0, column=12)

image_button_13 = Button(frame_cards_player, image=(unused_resize_cards_list[12]), bg="green", bd=0,
                         fg="green",
                         command=lambda: [image_button_13.grid_forget(), cards_in_the_middle(12)],
                         state=NORMAL)
image_button_13.grid(row=0, column=13)

window.mainloop()
