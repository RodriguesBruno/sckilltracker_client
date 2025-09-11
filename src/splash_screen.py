import time
import threading
import tkinter as tk
from PIL import ImageTk, Image


def show_splash_screen(duration=2) -> None:
    def splash():
        splash_root = tk.Tk()
        splash_root.overrideredirect(True)
        splash_root.wm_attributes("-topmost", True)
        splash_root.attributes("-alpha", 0.0)

        try:
            image = Image.open("static/splash.jpg")
            photo = ImageTk.PhotoImage(image)
            width, height = photo.width(), photo.height()

        except Exception:
            width, height = 400, 300
            photo = None

        screen_width = splash_root.winfo_screenwidth()
        screen_height = splash_root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        splash_root.geometry(f"{width}x{height}+{x}+{y}")

        if photo:
            canvas = tk.Canvas(splash_root, width=width, height=height, highlightthickness=0, bg="white")
            canvas.pack()
            canvas.create_image(0, 0, anchor="nw", image=photo)
            splash_root.image = photo
        else:
            tk.Label(splash_root, text="Loading...", font=("Helvetica", 18), bg="white").pack(expand=True)

        # Fade in
        def fade_in():
            for i in range(0, 21):
                splash_root.attributes("-alpha", i / 20)
                time.sleep(0.01)

        # Fade out
        def fade_out():
            for i in range(20, -1, -1):
                splash_root.attributes("-alpha", i / 20)
                time.sleep(0.01)

        def run_fade():
            fade_in()
            time.sleep(duration)
            fade_out()
            splash_root.destroy()

        threading.Thread(target=run_fade, daemon=True).start()
        splash_root.mainloop()

    threading.Thread(target=splash).start()