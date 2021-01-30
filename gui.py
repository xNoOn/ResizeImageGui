import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=600)
canvas.grid(columnspan=5, rowspan=5)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a Imgae on your computer to resize it", font="Raleway")
instructions.grid(columnspan=5, column=0, row=1)


def open_file():
        browse_text.set("loading...")
        file = askopenfile(parent=root, mode='rb', title="Choose a image file", filetype=[('Image Files', ['.jpeg', '.jpg', '.png', '.gif','*'])])
        if file:
            read_image = Image.open(file)
            browse_text.set("Browse")

            #Resize image to 300x300
            newsize = (300, 300)
            resize_image = read_image.resize(newsize)
            
            #Display Image on screen
            rs_image = ImageTk.PhotoImage(resize_image)
            rs_label = tk.Label(image=rs_image)
            rs_label.image = rs_image
            rs_label.grid(column=2, row=3)
                      


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#e20074", fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

#save button
save_text = tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text, command=lambda:save_file(), font="Raleway", bg="#e20074", fg="white", height=2, width=15)
save_text.set("Save")
save_btn.grid(column=2, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)


root.mainloop()