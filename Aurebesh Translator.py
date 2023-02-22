import tkinter as tk
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Aurebesh Translator App")
root.geometry("400x300")

# Set the font to the desired font pack
symbol_font = tk.font.Font(family="Aurebesh", size=14)

# Create a Text widget to display the translated text
result_text = tk.Text(root, height=2, font=symbol_font)
result_text.pack()

# Create a entry field for the user's guess
word_entry = tk.Entry(root)
word_entry.pack()

# Create a button to submit the user's phrase
def translate():
    # Copy the user's input to the result text widget
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, word_entry.get() + "\n")

    # Translate the input into symbols using the font pack
    translated_text = ""
    for char in word_entry.get():
        translated_char = symbol_font.charmap.get(ord(char), char)
        translated_text += translated_char

    # Insert the translated text into the result text widget
    result_text.insert(tk.END, translated_text + "\n")

language_button = tk.Button(root, text="Click me to Translate", command=translate)
language_button.pack()

# Create a button to clear the result and entry field
def clear():
    result_text.delete("1.0", tk.END)
    word_entry.delete(0, tk.END)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack()

# Start the GUI event loop
root.mainloop()
