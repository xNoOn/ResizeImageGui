import tkinter as tk
from tkinter import Label, Button, StringVar, BOTH, Frame, messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.image = None
        
        #Logo
        load = Image.open("C:/Users/nicos/OneDrive/Projekte/Dev/ImageResize/logo.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=100, y=10)

        #Instructions
        instructions = Label(master, text="Select a Image on your computer to resize it", font="Raleway")
        instructions.place(x=55, y=80)

        #Browse button
        browse_text = StringVar()
        browse_btn = Button(master, textvariable=browse_text, command=lambda:open_file(self), font="Raleway", bg="#e20074", fg="white", height=2, width=15)
        browse_text.set("Browse")
        browse_btn.place(x=59, y=120)

        #Save button
        save_text = StringVar()
        save_btn = Button(master, textvariable=save_text, command=lambda:save_file(self), font="Raleway", bg="#e20074", fg="white", height=2, width=15)
        save_text.set("Save")
        save_btn.place(x=214, y=120)

        def open_file(self):
            try:
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
            except Exception as ex:
                messagebox.showerror("Error","Something went wrong, try again please!")
                browse_text.set("Browse")
                print(ex)


        def save_file(self):
            try:
                if self.image:
                    save_text.set("loading...")
                    files = [('GIF', '*.gif'), ('PNG', '*.png'),('All Files', '*.*')] 
                    file = asksaveasfile( title="Save Resized Image", filetypes = files, defaultextension = files) 
                    if file:
                        self.image.save(file.name)
                        save_text.set("Save")
                        messagebox.showinfo("Information","Image saved!")
                        reset(self)
            except Exception as ex:
                messagebox.showerror("Error","Something went wrong, try again please!")
                save_text.set("Save")
                print(ex)

        def reset(self, master=None):
            try:
                self.image = None
                labelcount = 0

                for widget in self.master.winfo_children():
                    if widget.widgetName == "label":  
                        labelcount += 1
                        if labelcount == 2:   
                            widget.destroy()
            except Exception as ex:
                print(ex)

root = tk.Tk()
app = Window(root)
root.wm_title("Resize Image")
root.iconbitmap("C:/Users/nicos/OneDrive/Projekte/Dev/ImageResize/favicon.ico")
root.geometry("400x530")
root.mainloop()
