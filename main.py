from database_manager import DatabaseManager
from image_manager import ImageManager
from PIL import Image, ImageTk
import sys
import io
import tkinter as tk


class Application(tk.Frame):
    """
    This class is used to created the desktop application
    """
    DEFAULT_TITLE = "From Binary to image files"
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 600
    PRIMARY_COLOR = "#333"
    SECONDARY_COLOR = "#444"
    TERTIARY_COLOR = "white"
    IMAGE_PER_ROW = 3

    def __init__(self, master=None):
        """
        Initializes the window
        """
        super().__init__(master)
        self.app = master
        self.app.title(self.DEFAULT_TITLE)
        self.app.rowconfigure(0, minsize=self.DEFAULT_HEIGHT, weight=1)
        self.app.columnconfigure(1, minsize=self.DEFAULT_WIDTH, weight=1)
        self.frame_canvas = None
        self.frame_buttons = None
        self.images = None

        self.displayFrameButtons()
        self.displayFrameCanvas()

    def displayFrameButtons(self):
        """
        Display frame buttons on left side
        """
        self.frame_buttons = tk.Frame(self.app, width=200, bg=self.SECONDARY_COLOR)
        button_fetch = tk.Button(
            self.frame_buttons,
            text="Fetch Images",
            fg=self.TERTIARY_COLOR,
            bg=self.PRIMARY_COLOR,
            command=self.fetchImages
        )
        button_save_all = tk.Button(
            self.frame_buttons,
            text="Save All",
            fg=self.TERTIARY_COLOR,
            bg=self.PRIMARY_COLOR,
            command= lambda: self.saveAllImages(self.images)
        )
        button_quit = tk.Button(
            self.frame_buttons,
            text="Quit",
            fg=self.TERTIARY_COLOR,
            bg=self.PRIMARY_COLOR,
            command=self.app.destroy
        )

        button_fetch.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
        button_save_all.grid(row=1, column=0, sticky="ew", padx=5)
        button_quit.grid(row=2, column=0, sticky="ew", padx=5, pady=10)

        self.frame_buttons.grid(row=0, column=0, sticky="ns")

    def displayFrameCanvas(self):
        """
        Display frame canvas on right side
        """
        self.frame_canvas = tk.Frame(self.app, bg=self.PRIMARY_COLOR)
        self.frame_canvas.grid(row=0, column=1, sticky="nsew")

    def fetchImages(self):
        """
        Fetch images from Database and display them in frame canvas
        """
        imageIndex = 0
        db = DatabaseManager()
        self.images = db.find_signals_images()

        for i in range(0, len(self.images)):
            if i >= self.IMAGE_PER_ROW:
                break

            for j in range(self.IMAGE_PER_ROW):
                frame = tk.Frame(
                    master=self.frame_canvas,
                    relief=tk.FLAT,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)

                with Image.open(io.BytesIO(self.images[imageIndex][1]), "r") as imagePIL:
                    imagePIL.thumbnail((200, 200 * imagePIL.size[1] / imagePIL.size[0]))
                    canvas = tk.Canvas(master=frame, width=200, height=200)
                    canvas.pack(padx=5, pady=5)
                    frame.img = img = ImageTk.PhotoImage(image=imagePIL)
                    canvas.create_image(100, 100, anchor="center", image=img)

                imageIndex += 1

    def saveAllImages(self, images):
        """
        Save all of the files in _image_creator folder
        :param images: the list of the images to create
        """
        im = ImageManager()
        im.createAllImagesFiles(images)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
