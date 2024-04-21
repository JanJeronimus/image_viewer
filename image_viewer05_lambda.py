import tkinter as tk
from PIL import ImageTk, Image

class PictureViewerApp:
    """
    A simple picture viewer application using Tkinter.

    This application allows users to view different pictures and toggle the visibility of the picture frame.

    Attributes:
        master (tk.Tk): The main Tkinter window.
        plugin_frame (tk.Frame): The frame to display the pictures.
        current_image (Image): The currently displayed image.
        menu_bar (tk.Menu): The main menu bar.
        frame_menu (tk.Menu): Submenu for frame options.
        picture_menu (tk.Menu): Submenu for picture options.
    """

    def __init__(self, master):
        """
        Initialize the PictureViewerApp.

        Args:
            master (tk.Tk): The main Tkinter window.
        """
        self.master = master
        master.title("Picture Viewer Example")

        # Create a frame inside the main window
        self.plugin_frame = tk.Frame(master, padx=20, pady=20)
        self.plugin_frame.pack()

        # Load initial image
        self.current_image = Image.open("img\image1.png")
        self.display_image()

        # Create menu
        self.create_menu()

    def create_menu(self):
        """
        Create the main menu bar and its submenus.
        """
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Frame submenu
        self.frame_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.frame_menu.add_command(label="Show", command=self.show_frame)
        self.frame_menu.add_command(label="Hide", command=self.hide_frame)
        self.frame_menu.add_separator()
        self.frame_menu.add_command(label="Toggle", command=self.toggle_frame)
        self.frame_menu.add_separator()
        self.frame_menu.add_command(label="Exit", command=exit)

        # Pictures submenu
        self.picture_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.picture_menu.add_command(label="Picture 1", command=lambda: self.load_image("img\image1.png"))
        self.picture_menu.add_command(label="Picture 2", command=lambda: self.load_image("img\image2.png"))
        self.picture_menu.add_command(label="Picture 3", command=lambda: self.load_image("img\image3.png"))
        self.picture_menu.add_command(label="Picture 4", command=lambda: self.load_image("img\image04.png"))
        self.picture_menu.add_command(label="Image 5", command=lambda: self.load_image("img\image5.png"))

        self.menu_bar.add_cascade(label="Frame", menu=self.frame_menu)
        self.menu_bar.add_cascade(label="Pictures", menu=self.picture_menu)

    def load_image(self, filename):
        """
        Load an image file and display it in the frame.

        Args:
            filename (str): The path to the image file.
        """
        self.current_image = Image.open(filename)
        self.display_image()

    def display_image(self):
        """
        Display the current image in the frame.
        """
        # Clear the frame
        for widget in self.plugin_frame.winfo_children():
            widget.destroy()

        # Resize the image to fit the frame
        resized_image = self.current_image.resize((400, 300), Image.BILINEAR)
        photo = ImageTk.PhotoImage(resized_image)

        # Display the image in a label
        image_label = tk.Label(self.plugin_frame, image=photo)
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.pack()

    def show_frame(self):
        """
        Show the picture frame.
        """
        self.plugin_frame.pack()

    def hide_frame(self):
        """
        Hide the picture frame.
        """
        self.plugin_frame.pack_forget()

    def toggle_frame(self):
        """
        Toggle the visibility of the picture frame.
        """
        if self.plugin_frame.winfo_ismapped():
            self.hide_frame()
        else:
            self.show_frame()

# Create the main window and run the application
root = tk.Tk()
app = PictureViewerApp(root)
root.mainloop()
