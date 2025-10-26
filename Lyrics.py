import tkinter as tk

lyrics = [ 
     ("write lyrics here 1", "4"),
    ( "write lyrics here 2 ", "4"),
#YOU CAN WRITE ANY LYRICS FOR EXAMPLE 3,4,ETC 
]
root = tk.Tk()
root.title("Title")
root.geometry("600x200")

label = tk.Label(root, text=".Loading ...", font=("Arial", 20), wraplength=500, justify="center")
label.pack(expand=True, pady=20)

def show_lyrics(index=0):
    if index < len(lyrics):
        text, delay = lyrics[index]
        
        label.config(text=text)
        
        delay_in_ms = int(delay) * 1000 
        
        root.after(delay_in_ms, show_lyrics, index + 1)
        
    else:
        label.config(text="the end")

root.after(1000, show_lyrics, 0)

root.mainloop()