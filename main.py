import pyshorteners
import tkinter as tk

# Create a function to shorten the URL
def shorten_url():
    url = url_entry.get()
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(url)
    result_label.config(text=shortened_url)

# Create the GUI window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("620x620")
root.configure(bg="#0d1117")
root.resizable(False, False)

# Create the widgets
url_label = tk.Label(root, text="Enter URL to shorten:", bg="#0d1117", fg="#c9d1d9", font=("Helvetica", 14))
url_entry = tk.Entry(root, width=25, bg="#161b22", fg="#c9d1d9", font=("Helvetica", 14))
shorten_button = tk.Button(root, text="Shorten", bg="#238636", fg="#c9d1d9", font=("Helvetica", 14), command=shorten_url)
result_label = tk.Label(root, bg="#0d1117", fg="#c9d1d9", font=("Helvetica", 14))

# Add the widgets to the window
url_label.grid(row=0, column=0, padx=10, pady=10)
url_entry.grid(row=0, column=1, padx=10, pady=10)
shorten_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()