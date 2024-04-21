import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageViewer(tk.Tk):
    def __init__(self, initial_width, initial_height):
        super().__init__()

        self.title("Image Viewer")

        # Create the initial image label
        self.image_label = tk.Label(self)
        self.image_label.pack(side=tk.LEFT, padx=10, pady=10)

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

    def button1_click(self):
        print("Button 1 clicked")
        self.load_image("image1.png", self.winfo_width(), self.winfo_height())

    def button2_click(self):
        print("Button 2 clicked")
        self.load_image("image2.png", self.winfo_width(), self.winfo_height())

    def button3_click(self):
        print("Button 3 clicked")
        self.load_image("image3.png", self.winfo_width(), self.winfo_height())

    def button4_click(self):
        print("Button 4 clicked")
        self.load_image("image4.png", self.winfo_width(), self.winfo_height())

if __name__ == "__main__":
    initial_width, initial_height = 400, 300
    app = ImageViewer(initial_width, initial_height)
    app.mainloop()
