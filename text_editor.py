from tkinter import Tk, Text, Menu, filedialog, messagebox, font, simpledialog, colorchooser

# Dictionary of word replacements
replacements = {
    'teh': 'the',
    'mispell': 'misspell',
    'acress': 'across',
    # Add more word replacements as needed
}

def new_file():
    text.delete('1.0', 'end')

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file is not None:
        contents = file.read()
        text.delete('1.0', 'end')
        text.insert('1.0', contents)
        file.close()

def save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file is not None:
        data = text.get('1.0', 'end-1c')
        file.write(data)
        file.close()

def exit_editor():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def change_text_size():
    size = simpledialog.askinteger("Change Text Size", "Enter the text size:")
    if size is not None:
        text.configure(font=(current_font, size))

def replace_text():
    find_text = simpledialog.askstring("Replace Text", "Enter the word to find:")
    if find_text is not None:
        replace_text = simpledialog.askstring("Replace Text", "Enter the word to replace with:")
        if replace_text is not None:
            text_content = text.get('1.0', 'end-1c')
            updated_content = text_content.replace(find_text, replace_text)
            text.delete('1.0', 'end')
            text.insert('1.0', updated_content)

def make_text_bold():
    bold_font = font.Font(text, text.cget("font"))
    bold_font.configure(weight="bold")
    text.tag_configure("bold", font=bold_font)
    text.tag_add("bold", "sel.first", "sel.last")

def make_text_underline():
    underline_font = font.Font(text, text.cget("font"))
    underline_font.configure(underline=True)
    text.tag_configure("underline", font=underline_font)
    text.tag_add("underline", "sel.first", "sel.last")

def change_text_color():
    color = colorchooser.askcolor(title="Select Text Color")
    if color[1] is not None:
        text.tag_configure("color", foreground=color[1])
        text.tag_add("color", "sel.first", "sel.last")

def correct_text():
    text_content = text.get('1.0', 'end-1c')
    for word, replacement in replacements.items():
        text_content = text_content.replace(word, replacement)
    text.delete('1.0', 'end')
    text.insert('1.0', text_content)

root = Tk()
root.title("Text Editor")

text = Text(root, wrap='word')
text.pack(expand=True, fill='both')

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_editor)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Change Text Size", command=change_text_size)
editmenu.add_command(label="Replace Text", command=replace_text)
editmenu.add_separator()
editmenu.add_command(label="Make Text Bold", command=make_text_bold)
editmenu.add_command(label="Make Text Underline", command=make_text_underline)
editmenu.add_command(label="Change Text Color", command=change_text_color)
editmenu.add_command(label="Correct Text", command=correct_text)
menubar.add_cascade(label="Edit", menu=editmenu)

current_font = font.nametofont(text['font']).actual()['family']

root.config(menu=menubar)
root.mainloop()
