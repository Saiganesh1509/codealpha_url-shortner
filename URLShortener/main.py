import tkinter as tk
from tkinter import messagebox
import pyshorteners

class URLShortenerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("URL Shortener")

        self.create_widgets()

    def create_widgets(self):
        self.url_label = tk.Label(self.master, text="Enter URL:",width=100, height=5)
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(self.master, width=100 )
        self.url_entry.pack(pady=10)

        self.shorten_button = tk.Button(self.master, text="Shorten URL",background='#29C5F6', command=self.shorten_url,)
        self.shorten_button.pack(pady=10)

        self.short_url_label = tk.Label(self.master, text="Shortened URL:",width=100, height=5)
        self.short_url_label.pack()

    def shorten_url(self):
        long_url = self.url_entry.get()
        if long_url:
            try:
                s = pyshorteners.Shortener()
                short_url = s.tinyurl.short(long_url)
                self.display_short_url(short_url)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a valid URL.")

    def display_short_url(self, short_url):
        self.short_url_label.config(text=f"Shortened URL: {short_url}")

if __name__ == "__main__":
    root = tk.Tk()
    url_shortener_app = URLShortenerApp(root)
    root.mainloop()
