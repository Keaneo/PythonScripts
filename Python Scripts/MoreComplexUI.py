import json
import tkinter as tk
from PIL import ImageTk, Image
import cv2
from threading import Thread
import os

with open(os.path.dirname(os.path.abspath(__file__)) + r'\config.json') as file:
    data = json.load(file)
    
MenuNames = data['menuCascade']
camID = data['cameraId']


class WebcamInput:
    def __init__(self, src=0):
        self.videocap = cv2.VideoCapture(camID)
        while(not self.videocap.isOpened):
            #do nothing lol
            print("Not open")
        self.ret, self.frame = self.videocap.read() 
        self.stopped = False   
        self.width = self.videocap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def update(self):
        if self.stopped:
            return
        self.ret, self.frame = self.videocap.read()

    def read(self):
        self.update()
        return self.frame

    def stop(self):
        self.stopped = True

    def __del__(self):
        if self.videocap.isOpened():
            self.videocap.release()
        #self.window.mainloop()



showingCam = True




class Window:
    def __init__(self, window, window_title, src=0):
        WI = WebcamInput(src)
        
        self.window = window
        self.window.title(window_title)
        self.vid = WI
        self.read = self.vid.read()
        #root = tk.Tk()
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.filemenu=tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Exit', command=self.window.quit)

        self.frame = tk.Frame(self.window)
        self.frame.pack(side=tk.LEFT)
        self.canvas = tk.Canvas(self.frame, width=self.vid.width, height=self.vid.height)
        self.canvas.pack(side = tk.TOP)
        #read = WI.read()
        self.img = self.processImage(self.read)
        self.canvas.create_image(1,1,anchor=tk.NW, image=self.img)
        self.delay = 5
        self.update()

        self.window.mainloop()

    def update(self):
        self.read = self.vid.read()
        self.img = self.processImage(self.read)
        self.canvas.create_image(1,1,image=self.img, anchor=tk.NW)

        #Do stuff before this line
        self.window.after(self.delay, self.update)

    def processImage(self, img):
        read = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(read)
        img = ImageTk.PhotoImage(image=im)
        return img
        #self.canvas.create_image(1,1,anchor=tk.NW, image=img)

Window(tk.Tk(), "Window!", 0)
