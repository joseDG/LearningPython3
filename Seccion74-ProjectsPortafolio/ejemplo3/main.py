import tkinter.messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

img_url = ""
watermarked_img = None

window = Tk()
window.title("Watermark Your Images!")
window.config(padx=50, pady=50, bg="#EEEEEE")

# ------------ Title Text ------------- #
title = Label(text="Watermarker", font=(
    'Verdana', 30))
title.config(bg="#EEEEEE", fg="#000000", pady=10)
title.grid(row=0, column=0, columnspan=2)


def show_img():
    # Via button
    # Open finder for the image to copyright
    # If file valid (in a supported img file)
    # Then show the image
    window.withdraw()
    global img_url
    img_url = askopenfilename(filetypes=[('Image Files', '*.png')])

    if img_url is not None:
        img = ImageTk.PhotoImage(Image.open(img_url).resize((480, 270), Image.ADAPTIVE))
        label = Label(window, image=img)
        label.image = img
        label.config(pady=100)
        label.grid(row=2, column=0, columnspan=2)
        window.deiconify()


def copyright_img():
    # Combine the 2 img provided
    # Then Create a New Image
    watermark = Image.open(
        "/Users/edward/Developer/PycharmProjects/Watermarking_Desktop_App/icons/no_copyright_icon.png").resize(
        (100, 100),
        Image.ADAPTIVE)
    try:
        img = Image.open(img_url).resize((480, 270), Image.ADAPTIVE)

        img.paste(watermark, (250, 120), watermark)
        """Image.paste(im, box=None, mask=None)"""
        global watermarked_img
        watermarked_img = ImageTk.PhotoImage(img)

        label = Label(window, image=watermarked_img)
        label.image = watermarked_img
        label.grid(row=2, column=0, columnspan=2)


    except AttributeError:
        print("Please Upload file first")
        tkinter.messagebox.showerror(title="Error",
                                     message="Please Upload file first")


# Alert Error "Please Upload file first"


def download_img():
    # Resize the copyright image back to its original size
    # Ask user for the location to store the image
    try:
        image = ImageTk.getimage(watermarked_img)
        image = image.resize((3840, 2160))

        image.save("/Users/edward/Desktop/merged_image.png", "PNG")
        print("Image Saved")
        image.show()
    except AttributeError:
        tkinter.messagebox.showerror(title="Error",
                                     message="Please Upload file first")


def quit_program():
    window.destroy()


# ----------- Upload Location Button ---------#
upload_img_icon = PhotoImage(file="../icons/upload_icon.png")
upload_img_icon = upload_img_icon.subsample(120, 120)

upload_img_btn = Button(
    image=upload_img_icon,
    text="Upload File",
    compound=LEFT,
    highlightthickness=0,
    bg="#FFFFFF",
    command=show_img,
    padx=20
)

upload_img_btn.grid(row=1, column=0)

# ------------ Copyright Button -----------------#
copyright_img_icon = PhotoImage(file="../icons/no_copyright_icon.png")
copyright_img_icon = copyright_img_icon.subsample(120, 120)

copyright_btn = Button(
    window,
    image=copyright_img_icon,
    compound=LEFT,
    text="Watermark",
    highlightthickness=0,
    bg="#FFFFFF",
    padx=20,
    command=copyright_img
)
copyright_btn.grid(row=1, column=1)

# ------------ Download Button -----------------#
download_img_icon = PhotoImage(
    file="/Users/edward/Developer/PycharmProjects/Watermarking_Desktop_App/icons/download_icon.png")
download_img_icon = download_img_icon.subsample(120, 120)
download_img_btn = Button(
    window,
    image=download_img_icon,
    text="Download File",
    compound=LEFT,
    bg="#FFFFFF",
    padx=64,
    highlightthickness=0,
    command=download_img
)
download_img_btn.grid(row=3, column=0, columnspan=2)

# -------------Quit Program ------------ #
quit_icon = PhotoImage(
    file="/Users/edward/Developer/PycharmProjects/Watermarking_Desktop_App/icons/quit_icon.png")
quit_icon = quit_icon.subsample(120, 120)
quit_btn = Button(
    window,
    image=quit_icon,
    text="Quit Program",
    compound=LEFT,
    bg="#FFFFFF",
    padx=65,
    highlightthickness=0,
    command=quit_program
)
quit_btn.grid(row=4, column=0, columnspan=2)

window.mainloop()