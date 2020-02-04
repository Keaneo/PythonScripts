from tkinter import *
import baseconvert

window = Tk()

def convert(e1,e2,e3, label):
    output = baseconvert.base(int(e1.get()), int(e2.get()), int(e3.get()))
    #outputNUM.set(str(output))
    #window.update_idletasks()
    newOutput = ""
    for item in output:
        newOutput += str(item)
    print(str(newOutput))
    label.config(text=str(newOutput))
    window.update_idletasks()
    #return output

window.title("Number Converter")

Label(window, text="Number To Convert").grid(row=0)
Label(window, text="Base of Input").grid(row=1)
Label(window, text="Base of Output").grid(row=2)
Label(window, text="Output Number = ").grid(row=4)
outputNUM = StringVar()
outputNumberDisplay = Label(window, text="Enter Something")
outputNumberDisplay.grid(column = 1,row=4)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

e1.grid(row=0, column= 1)
e2.grid(row=1, column= 1)
e3.grid(row=2, column= 1)

goButton = Button(window, text='Go', width=20)
goButton.grid(row=3)
goButton.config(command=lambda:convert(e1,e2,e3, label=outputNumberDisplay) )

#print(returned)




window.mainloop()


