import tkinter as tk
import cv2

videocap = cv2.VideoCapture(0)

root = tk.Tk()
menu = tk.Menu(root)
root.config(menu=menu)
filemenu=tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)

frame = tk.Frame(root)
frame.pack(side=LEFT)
canvas = tk.Canvas(frame, width=640, height=480)
canvas.pack(side = TOP)
canvas.create_image(1,1,anchor=N, image=videocap.read())


tk.mainloop()
