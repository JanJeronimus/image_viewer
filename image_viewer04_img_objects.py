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

        # Store all ImageObject instances
        self.all_image_objs = []

    def add_image_objects(self):
        """Add all ImageObject instances."""
        global_vars = globals()
        image_objs = [var for var in global_vars.values() if isinstance(var, ImageObject)]
        for image_obj in image_objs:
            self.all_image_objs.append(image_obj)
            self.create_button(image_obj)

    def create_button(self, image_obj):
        """Create button for a given image object."""
        button_text = os.path.splitext(image_obj.path)[0]  # Use filename as button text
        button = tk.Button(self.button_frame, text=button_text, command=lambda obj=image_obj: self.load_image(obj))
        button.pack(fill=tk.X, padx=5, pady=5)

    def load_image(self, image_obj):
        """Load and display the image associated with the given image object."""
        if os.path.exists(image_obj.path):
            # Load and display the image
            image = Image.open(image_obj.path)
            image.thumbnail((self.winfo_width(), self.winfo_height()))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo, text="")
            # Keep reference to photo to prevent garbage collection
            self.image_label.image = photo
        else:
            # Remove existing image and display error message
            self.image_label.config(image="", text=f"Error: Image '{image_obj.path}' not found", fg="red")

class ImageObject:
    def __init__(self, path):
        self.path = path

if __name__ == "__main__":
    initial_width, initial_height = 400, 300
    
    # Define ImageObject instances
    img1 = ImageObject("img/image1.png")
    img2 = ImageObject("img/image2.png")
    img3 = ImageObject("img/image3.png")
    img4 = ImageObject("img/image4.png")
    
    # Create ImageViewer instance
    app = ImageViewer(initial_width, initial_height)
    
    # Add all ImageObject instances to ImageViewer and create buttons automatically
    app.add_image_objects()
    
    app.mainloop()
