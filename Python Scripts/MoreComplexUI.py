import json
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
import threading
import os
import numpy as np
from infi.systray import SysTrayIcon

#region JSON Reading

class JSONStuff:
    
    with open(os.path.dirname(os.path.abspath(__file__)) + r'\config.json') as file:
        data = json.load(file)
        
    MenuNames = data['menuCascade']
    camID = data['cameraId']
    showingCam = data['showCam']
    camRes = data['camRes']
    delay = data['delay']
    followHead = data['followHead']
    iconPath = data['iconPath']
    print(followHead)

    def save(self):
        newData = {'menuCascade': self.MenuNames, 'cameraId': self.camID, 'showCam':self.showingCam, 'camRes': self.camRes, 'delay': self.delay, 'followHead':self.followHead, 'iconPath':self.iconPath} 
        print(self.followHead)
        with open(os.path.dirname(os.path.abspath(__file__)) + r'\config.json', 'w') as outfile:
            json.dump(newData, outfile,indent=4)

#endregion

#region JSON Writing


#endregion

#region Standalone Methods

#region Changing Camera Resolution :: TO-DO!
# def getCamAspectRatio():
#     return cv2.CAP_PROP_FRAME_HEIGHT / cv2.CAP_PROP_FRAME_WIDTH

# def calcNewCamRes(newVal, isWidth : bool):
#     if isWidth:
#         return int(float(newVal) / aspectRatio)
#     else:
#         return int(float(newVal) * aspectRatio)

# def getNewWidthCallback(window, val=0):
#     #window.vid.videocap.release()
#     #window.vid.videocap.set(cv2.CAP_PROP_FRAME_WIDTH, val)
#     #window.vid.videocap.set(cv2.CAP_PROP_FRAME_HEIGHT, calcNewCamRes(val, True))
#     #window.vid.videocap.open(JSONStuff.camID)
#     updatedCamWidth = 0
#     if val == 0:
#         updatedCamWidth = window.camResolutionWidth.get()
#     else:
#         updatedCamWidth = val

#     print(str(updatedCamWidth) + " " + str(calcNewCamRes(updatedCamWidth,True)))
#     return int(updatedCamWidth)
#     #print(str(window.vid.videocap.get(cv2.CAP_PROP_FRAME_WIDTH)) + " " + str(window.vid.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# def getNewHeightCallback(window, val=0):
#     #window.vid.videocap.release()
#     #window.vid.videocap.set(cv2.CAP_PROP_FRAME_HEIGHT, val)
#     #window.vid.videocap.set(cv2.CAP_PROP_FRAME_HEIGHT, calcNewCamRes(val, False))
#     #window.vid.videocap.open(JSONStuff.camID)
#     updatedCamHeight = 0
#     if val == 0:
#         updatedCamHeight = window.camResolutionHeight.get()
#         #print(updatedCamHeight)        
#     else:
#         updatedCamHeight = val
        
    
#     print(str(updatedCamHeight) + " " + str(calcNewCamRes(updatedCamHeight,False)))
#     return int(updatedCamHeight)
    


# def setNewCamResolution(window):
    
#     updatedCamHeight = getNewHeightCallback(window=window)
#     updatedCamWidth = getNewWidthCallback(window=window)
#     window.vid.videocap.release()
#     print(updatedCamHeight)
#     window.vid.videocap.set(cv2.CAP_PROP_FRAME_HEIGHT, updatedCamHeight)
#     print(window.vid.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     window.vid.videocap.set(cv2.CAP_PROP_FRAME_WIDTH, updatedCamWidth)
#     window.vid.videocap.open(JSONStuff.camID)
#     print(str(window.vid.videocap.get(cv2.CAP_PROP_FRAME_WIDTH)) + " " + str(window.vid.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    
#endregion


#endregion

#region Global Variables

#aspectRatio = getCamAspectRatio()
#updatedCamWidth = 0
#updatedCamHeight = 0

#endregion


#region Classes

class WebcamInput:
    def __init__(self, src=0):
        self.videocap = cv2.VideoCapture(JSONStuff.camID)
        while(not self.videocap.isOpened):
            #do nothing lol
            print("Not open")
        self.ret, self.frame = self.videocap.read() 
        self.stopped = False   
        #self.width = self.videocap.get(cv2.CAP_PROP_FRAME_WIDTH)
        #self.height = self.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #self.videocap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        #self.videocap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)

    def start(self):
        threading.Thread(target=self.update, args=()).start()
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
        
def _closingWindow(window):
    JSONStuff.save()
    if messagebox.askokcancel("Minimizing to Tray", "Minimizing, Are you sure?"):
        #window.destroy()
        window.sysTray.Hide()

def _closingProgram(window=None):    
    if window is not None:
        window.window.destroy()
        print('ClosingWithWindow')
        exit(0)
    else:
        print('Closing')
        exit(0)

class SystemTrayFunctions:
    def __init__(self, window):
        self.window = window
        menuoptions = (("Show Options", None, lambda show: self.Show()),)
        self.systray = SysTrayIcon(JSONStuff.iconPath, "Peek", menuoptions, on_quit= lambda quit: _closingProgram(self.window))
        self.systray.start()

    def Show(self):
        self.window.window.wm_deiconify()
        self.window.vid.videocap.open(JSONStuff.camID)

    def Hide(self):
        print('Hiding!')        
        self.window.vid.videocap.release()
        self.window.canvas.delete('all')
        self.window.window.withdraw()

           


class Window:
    def __init__(self, window, window_title, JSONStuff, src=0):
        self.setup(window, window_title, src)      
        window.protocol("WM_DELETE_WINDOW", lambda: _closingWindow(self))
        #self.t = tk.Toplevel()
        window.bind("<Unmap>", self.OnUnmap)
        #window.bind("<Map>", self.OnMap)

        self.window.mainloop()

    def OnMap(self, event):
        # show the tool window
        self.window.wm_deiconify()

    def OnUnmap(self, event):
        # withdraw the tool window
        #self.window.wm_iconify()
        self.sysTray.Hide()

    def setup(self, window, window_title, sysTray, src=0):
        #Start Webcam
        WI = WebcamInput(src)        
        self.window = window
        self.window.title(window_title)
        self.window.geometry('1280x720')
        self.vid = WI          
         
        #Add File-type menus    
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.filemenu=tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Exit', command=self.window.quit)
        self.sysTray = SystemTrayFunctions(self)

        #Add Frame for layout (Video output)
        self.framevid = tk.Frame(self.window, width=self.vid.videocap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT), highlightbackground="black", highlightthickness=3)    
        #self.framevid.pack(anchor=tk.NW, padx=20, pady=20)
        self.framevid.grid(row=0, column=0, padx=20, pady=20)

        #Add Canvas to frame, this allows image display
        self.canvas = tk.Canvas(self.framevid, width=self.vid.videocap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.grid(sticky=tk.NW, row=0, column=0) 

        #Set delay, increase to use less processor power!
        self.delay = JSONStuff.delay #Must be in milliseconds!

        #Frame for buttons and other stuff
        self.framesettings = tk.Frame(self.window, highlightbackground="black", highlightthickness=3)
        self.framesettings.grid(row=0, column=1, padx=20,pady=20, sticky=tk.N)

        #Buttons!
        self.showCamButton = tk.Button(self.framevid, text='Stop Camera Preview' if JSONStuff.showingCam else 'Show Camera Preview', width=20)
        self.showCamButton.config(command=lambda: self.toggleCamPreview())
        self.showCamButton.grid(row=3, column=0)

        self.followHeadValue = tk.IntVar(value=JSONStuff.followHead )
        self.followHeadTick = tk.Checkbutton(self.framesettings, text='Follow Head Motion')
        self.followHeadTick.config(var = self.followHeadValue)
        self.followHeadTick.grid(row=1, column = 1)
        JSONStuff.followHead = self.followHeadValue.get()

        self.LeftTSValue = tk.IntVar()
        self.LeftThresholdSlider = tk.Scrollbar(self.framevid, orient='horizontal', command=self.LeftTSValue ).grid(row=1, column=0, sticky=tk.EW)
        self.LeftTSLabel = tk.Label(self.framevid, text="Set the Threshold for moving left!").grid(row=2, column=0, sticky=tk.W)




        #region Changing Cam Res stuff, come back to
        # self.setNewCamResButton = tk.Button(self.framesettings, text='Confirm New Resolution')
        # self.setNewCamResButton.config(command=lambda: setNewCamResolution(window=self))
        # self.setNewCamResButton.grid(row=2, column=2)

        
        # self.camResolutionWidth = tk.Entry(self.framesettings)
        # self.camResolutionHeight = tk.Entry(self.framesettings)
        # #self.camResolutionWidth.bind("<Return>", lambda event: getNewWidthCallback(int(self.camResolutionWidth.get()), window=self))
        # #self.camResolutionHeight.bind("<Return>", lambda event: getNewHeightCallback(int(self.camResolutionHeight.get()), window=self))
        # self.camResolutionWidthLabel = tk.Label(self.framesettings, text='Width')
        # self.camResolutionHeightLabel = tk.Label(self.framesettings, text='Height')

        # #Resolution picking text entry boxes
        # self.camResolutionWidth.grid(row=1,column=1)
        # self.camResolutionWidthLabel.grid(row=1, column=0)
        # self.camResolutionHeight.grid(row=1, column=4)
        # self.camResolutionHeightLabel.grid(row=1, column=3)
        #endregion

        #this comes last in setup
        threading.Thread(target=self.update).start()

    def update(self):
        #Takes a frame from webcam, converts to the right colour space and Tkinter compatible format, then displays
        if JSONStuff.showingCam:
            self.read = self.vid.read()
            self.img = self.processImage(self.read)
            self.canvas.create_image(1,1,image=self.img, anchor=tk.NW)        
        

        #Do stuff before this line
        self.window.after(self.delay, self.update)

    def toggleCamPreview(self):
        if JSONStuff.showingCam:
            self.showCamButton.config(text='Show Camera Preview')
            JSONStuff.showingCam = False
            self.img = self.processImage(np.zeros((int(self.vid.videocap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(self.vid.videocap.get(cv2.CAP_PROP_FRAME_HEIGHT)), 3), np.uint8))
            self.canvas.create_image(1,1,image=self.img)
        else:
            self.showCamButton.config(text='Stop Camera Preview')
            JSONStuff.showingCam = True
        print(JSONStuff.showingCam)


    def processImage(self, img):
        if not img is None:
            read = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(read)
            img = ImageTk.PhotoImage(image=im)
            return img
        #self.canvas.create_image(1,1,anchor=tk.NW, image=img)

    #def findResolutions(self, src=0):
    #    self.vid.videocap.get(cv2.CAP_PROP_)

#endregion
JSONStuff = JSONStuff()

window = Window(tk.Tk(), "Window!", JSONStuff=JSONStuff)





