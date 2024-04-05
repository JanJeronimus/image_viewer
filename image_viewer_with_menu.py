import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageViewerWithMenuAndButtons(tk.Tk):
    def __init__(self, initial_width, initial_height):
        super().__init__()

        self.title("Image Viewer with Menu and Buttons")

        # Create the initial image label
        self.image_label = tk.Label(self)
        self.image_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create the "File" menu
        file_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.exit_app)

        # Create the "Images" menu
        images_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Images", menu=images_menu)

        # Add "Show..." submenu for each image
        image_files = ["image1.png", "image2.png", "image3.png", "image4.png"]
        for image_file in image_files:
            images_menu.add_command(label=f"Show {image_file}", command=lambda file=image_file: self.show_image(file))

        # Create buttons on the right side
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        button_texts = ["Button 1", "Button 2", "Button 3", "Button 4"]
        button_commands = [self.button1_click, self.button2_click, self.button3_click, self.button4_click]

        for text, command in zip(button_texts, button_commands):
            button = tk.Button(self.button_frame, text=text, command=command)
            button.pack(fill=tk.X, padx=5, pady=5)

    def load_image(self, image_path, width, height):
        """Load and display the image with the given path, width, and height."""
        if os.path.exists(image_path):
            # Load and display the image
            self.image = Image.open(image_path)
            self.image.thumbnail((width, height))
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo, text="")
        else:
            # Remove existing image and display error message
            self.image_label.config(image="", text=f"Error: Image '{image_path}' not found", fg="red")

    def show_image(self, image_file):
        """Display the selected image."""
        self.load_image(image_file, self.winfo_width(), self.winfo_height())

    def button1_click(self):
        print("Button 1 clicked")
        self.show_image("image1.png")

    def button2_click(self):
        print("Button 2 clicked")
        self.show_image("image2.png")

    def button3_click(self):
        print("Button 3 clicked")
        self.show_image("image3.png")

    def button4_click(self):
        print("Button 4 clicked")
        self.show_image("image4.png")

    def exit_app(self):
        """Exit the application."""
        self.destroy()

if __name__ == "__main__":
    initial_width, initial_height = 400, 300
    app = ImageViewerWithMenuAndButtons(initial_width, initial_height)
    app.mainloop()
