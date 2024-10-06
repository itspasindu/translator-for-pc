import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Initialize the translator
translator = Translator()

def translate_text():
    # Get the input text and selected languages
    input_text = input_text_box.get("1.0", tk.END).strip()
    source_lang = source_lang_combo.get()
    target_lang = target_lang_combo.get()
    
    if input_text:
        # Detect language if source language is set to auto-detect
        if source_lang == "Auto Detect":
            detected_lang = translator.detect(input_text).lang
        else:
            detected_lang = source_lang

        # Perform translation
        translated = translator.translate(input_text, src=detected_lang, dest=target_lang)
        
        # Display the translated text
        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated.text)

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")

# Labels
title_label = tk.Label(root, text="Language Translator", font=("Arial", 18))
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="User input language with auto-detect option", font=("Arial", 10))
instruction_label.pack()

# Input and Output Text Boxes
input_text_box = tk.Text(root, height=5, width=50)
input_text_box.pack(pady=10)

output_text_box = tk.Text(root, height=5, width=50)
output_text_box.pack(pady=10)

# Language Selection Combobox
languages = ['Auto Detect', 'en', 'fr', 'es', 'de', 'zh-cn', 'ja', 'ko', 'ru']  # Add more languages if needed

# Source language combobox
source_lang_combo = ttk.Combobox(root, values=languages)
source_lang_combo.set("Select Language")
source_lang_combo.pack(side=tk.LEFT, padx=10)

# Target language combobox
target_lang_combo = ttk.Combobox(root, values=languages[1:])
target_lang_combo.set("Select Language")
target_lang_combo.pack(side=tk.RIGHT, padx=10)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=20)

# Footer Label
footer_label = tk.Label(root, text="Developed by Pasindu Dewviman", font=("Arial", 10))
footer_label.pack(side=tk.BOTTOM)

root.mainloop()
