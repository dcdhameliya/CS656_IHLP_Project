import tkinter as tk
from PIL import Image, ImageTk

r = tk.Tk()
r.title('A Game of Strategy')
r.geometry("1000x1000")
# r.configure(bg='white')

titleLabel = tk.Label(r, text="A Game of Strategy! Let's Play!")
ipLabel = tk.Label(r, text = "Enter Server IP to connect:").place(x = 30,y = 50)
connectButton = tk.Button(r, text = "Connect").place(x = 800, y = 50)  

startButton = tk.Button(r, text = "Play Game").place(x = 30, y = 100)  

ipText = tk.Entry(r,width = 20).place(x = 400, y = 50)

scoreLabel = tk.Label(r, text = "Your Current Score:").place(x = 30,y = 150)
scoreDisplayLabel = tk.Label(r, text = "0").place(x = 180,y = 150)

image1 = ImageTk.PhotoImage(Image.open("C_2.png").resize((300,505), Image.ANTIALIAS))

imageLabel = tk.Label(r, image = image1).place(x = 180,y = 200)

r.mainloop()