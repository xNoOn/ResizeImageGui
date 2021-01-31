from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.image = None
        
        #Logo
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        #Instructions
        instructions = Label(master, text="Select a Image on your computer to resize it", font="Raleway")
        instructions.place(x=55, y=80)

        #browse button
        browse_text = StringVar()
        browse_btn = Button(master, textvariable=browse_text, command=lambda:open_file(self), font="Raleway", bg="#e20074", fg="white", height=2, width=15)
        browse_text.set("Browse")
        browse_btn.place(x=59, y=120)

        #save button
        save_text = StringVar()
        save_btn = Button(master, textvariable=save_text, command=lambda:save_file(self), font="Raleway", bg="#e20074", fg="white", height=2, width=15)
        save_text.set("Save")
        save_btn.place(x=214, y=120)

        def open_file(self):
            browse_text.set("loading...")
            file = askopenfile(parent=master, mode='rb', title="Choose a image file", filetype=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif','*.*'])])
            if file:
                image = Image.open(file)
                newsize = (300,300)
                self.image = image.resize(newsize)
                browse_text.set("Browse")
                
                #Display Image on screen
                render = ImageTk.PhotoImage(self.image)
                img = Label(image=render)
                img.image = render
                img.place(x=55, y=200)

        def save_file(self):
            if self.image:
                save_text.set("loading...")
                files = [('GIF', '*.gif'), ('PNG', '*.png'), ('JPG', '*.jpg'),('All Files', '*.*')] 
                file = asksaveasfile( initialfile=self.image_name, title="Save Resized Image", filetypes = files, defaultextension = files) 
                
                print("file.name: ", file.name)
                if file:
                    #self.image.save("test.gif", format="gif")
                    self.image.save(file.name)
                    save_text.set("Image saved")
root = Tk()
app = Window(root)
root.wm_title("Resize Image")
root.geometry("400x530")
root.mainloop()