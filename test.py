from tkinter import *
import random
from PIL import Image, ImageTk


def resize_cards(card):
    entry_card = Image.open(card)
    resized_image = entry_card.resize((160, 230))
    global final_card
    final_card = ImageTk.PhotoImage(resized_image)
    return final_card


window = Tk()
window.geometry("1200x800")
window.configure(background="#008000")
window.iconbitmap(r'pictures/icon.ico')
info_menu = Menu(window)

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
frame_cards_middle.place(relx=0.5, rely=0.5, anchor=CENTER)

# title(0, 0)
# press_shuffle()
x_card = 0
num_lose = 0
num_win = 0

window.config(menu=info_menu)
frame_victory = Frame(window, bg='green')


# def aaaaa():
#     global panel_0
#     panel_0.grid_remove()
#     print("Hello......")
#
#
# def bbbb():
#     global panel_1
#     # panel_1.grid_remove()
#     print("Hello......")

def cards_in_the_middle(card):
    panel_0 = Label(frame_cards_middle, image=card, bg="black")
    panel_0.grid(row=0, column=0)


photos_cards_player = []

resized_card = resize_cards(f'images/C_2.png')
photos_cards_player.append(resized_card)

resized_card = resize_cards(f'images/C_3.png')
photos_cards_player.append(resized_card)

resized_card = resize_cards(f'images/C_4.png')
photos_cards_player.append(resized_card)

resized_card = resize_cards(f'images/C_5.png')
photos_cards_player.append(resized_card)

resized_card = resize_cards(f'images/C_6.png')
photos_cards_player.append(resized_card)

resized_card = resize_cards(f'images/C_7.png')
photos_cards_player.append(resized_card)

panel_0 = Button(frame_cards_player, image=photos_cards_player[0], bg="green", bd=0, fg="green",
                 command=lambda: [panel_0.grid_forget(), cards_in_the_middle(photos_cards_player[0])], state=NORMAL)
panel_0.grid(row=0, column=0)

panel_1 = Button(frame_cards_player, image=photos_cards_player[1], bg="green", bd=0,
                 command=lambda: [panel_1.grid_forget(), cards_in_the_middle(photos_cards_player[1])], state=NORMAL)
panel_1.grid(row=0, column=1)

panel_2 = Button(frame_cards_player, image=photos_cards_player[2], bg="green", bd=0,
                 command=lambda: [panel_2.grid_forget(), cards_in_the_middle(photos_cards_player[2])], state=NORMAL)
panel_2.grid(row=0, column=2)

panel_3 = Button(frame_cards_player, image=photos_cards_player[3], bg="green", bd=0,
                 command=lambda: [panel_3.grid_forget(), cards_in_the_middle(photos_cards_player[3])], state=NORMAL)
panel_3.grid(row=0, column=3)

panel_4 = Button(frame_cards_player, image=photos_cards_player[4], bg="green", bd=0,
                 command=lambda: [panel_4.grid_forget(), cards_in_the_middle(photos_cards_player[4])], state=NORMAL)
panel_4.grid(row=0, column=4)

window.mainloop()
