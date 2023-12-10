from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def add_watermark():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    image = Image.open(
        root.filename
    ).convert("RGBA")

    watermark_image =  image.copy()

    draw = ImageDraw.Draw(watermark_image)

    w, h = image.size
    x, y = int(w /2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    font = ImageFont.truetype(
        "FreeMono.ttf",
        int(font_size/6)
    )
    draw.text(
        (x, y),
        watermarktext.get(),
        fill=(255, 255, 255, 128),
        font=font,
        anchor="ms"
    )
    plt.subplot(
        1,2,2
    )
    plt.imshow(watermark_image)
    watermark_image.show()


window = Tk()
window.title("WaterMark")
window.config(padx=50, pady=50)

canvas = Canvas(
    width=100,
    height =100,
    highlightthickness=0
)
canvas.grid(
    column=4,
    row=4,
)
title = Label(
    text="Water Marking App"
)
title.grid(
    column=2,
    row=0,
)

watermarklabel = Label(
    text="Text for your watermark:"
)
watermarklabel.grid(
    column=2,
    row=2
)

watermarktext = Entry()
watermarktext.grid(
    column=3,
    row=2
)

add = Button(
    text="Add Watermark",
    highlightthickness=0,
    command=add_watermark
)

add.grid(
    column=3,
    row=3
)
window.mainloop()