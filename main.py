from database_manager import DatabaseManager
from image_manager import ImageManager
import sys
import tkinter


class Application(tkinter.Frame):
    """
    This class is used to created the desktop application
    """
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600

    def __init__(self, master=None):
        """
        Initializes the window
        """
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.create_label_widget("From Binary to Image", "top")
        self.create_button_widget("Fetch TMC Images", "top", self.fetchImages)

        self.create_button_widget("Quit", "bottom", self.master.destroy)

    def create_label_widget(self, text, pos, **options):
        label = tkinter.Label(self)
        label["text"] = text
        label.pack(side=pos)

        if options.get("fg"):
            label["fg"] = options.get("fg")

        if options.get("bg"):
            label["bg"] = options.get("bg")

    def create_button_widget(self, text, pos, command=None):
        button = tkinter.Button(self)
        button["text"] = text
        button["command"] = command
        button.pack(side=pos)

    def fetchImages(self):
        db = DatabaseManager()
        images = db.find_signals_images()
        for image in images:
            self.create_label_widget(image, "top", fg="white", bg="black")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()