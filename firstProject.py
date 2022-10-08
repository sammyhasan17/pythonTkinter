from tkinter import *

from PIL import Image
# creates our window, sometimes called root
window = Tk()
# set size
window.geometry("200x200")
window.iconbitmap('Desktop')


def buttonClicked():
    newLabel = Label(window)
    print("button was clicked")
    newLabel.pack()
    # open method used to open extension image file
    fileName = "/Users/sam/Downloads/Pictures/1.jpeg"
    im = Image.open(fileName)
    # This method will show image in any image viewer
    im.show()



# creates a label in our window, with some text


theButton = Button(window, text="click meh", command=buttonClicked, padx=10, pady=10)
theButton.pack()

# presents the root
window.mainloop()
print()
