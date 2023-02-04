from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox

root = Tk()


# Change Font Size
def font_size_chooser(e):
	our_font.config(size=font_size_listbox.get(font_size_listbox.curselection()))

# Change Font Style
def font_style_chooser(e):
	style = font_style_listbox.get(font_style_listbox.curselection()).lower()

	if style == "bold":
		our_font.config(weight=style)
	if style == "regular":
		our_font.config(weight="normal", slant="roman", underline=0, overstrike=0)
	if style == "italic":
		our_font.config(slant=style)
	if style == "underline":
		our_font.config(underline=1)
	
# Create Font Chooser Function
def font_chooser(e):
	our_font.config(family=my_listbox.get(my_listbox.curselection()))

# Designate Our Font
our_font = font.Font(family="Helvetica", size="32")

# Add Frame
my_frame = Frame(root, width=480, height=300)
my_frame.pack(pady=10)
# Freeze Frame In Place
my_frame.grid_propagate(False)
my_frame.columnconfigure(0, weight=10)

# Add Text Box
my_text = Text(my_frame, font=our_font)
my_text.grid(row=0, column=0)
my_text.grid_rowconfigure(0, weight=1)
my_text.grid_columnconfigure(0, weight=1)

# Create Menu
my_menu=Menu(root)
root.config(menu=my_menu)

# New File Function
def new_file():
	my_text.delete("1.0",END)
	root.title('Word Clone')

# Open File Function
def open_file():
	my_text.delete("1.0",END)
	text_file = filedialog.askopenfilename(title="Open File",filetypes=(("TextFiles","*.txt"),("Python Files","*.py"),("All Files","*.*")))
	text_file = open(text_file,'r')
	stuff = text_file.read()
	my_text.insert(END,stuff)
	text_file.close()

# Save File Function	
def save_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*",title="Save File",filetypes=(("TextFiles",".txt"),("Python Files",".py"),("All Files","*.*")))
	text_file = open(text_file,'w')
	text_file.write(my_text.get("1.0",END))
	text_file.close()

# Add File Menu
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Bottom Frame
bottom_frame = Frame(root)
bottom_frame.pack()

# Add Labels
font_label = Label(bottom_frame, text="Choose Font", font=("Helvetica", 16))
font_label.grid(row=0, column=0, padx=10, sticky=W)

size_label = Label(bottom_frame, text="Font Size", font=("Helvetica", 16))
size_label.grid(row=0, column=1, sticky=W)

style_label = Label(bottom_frame, text="Font Style", font=("Helvetica", 16))
style_label.grid(row=0, column=2, padx=10, sticky=W)

# Add Listbox
my_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=40)
my_listbox.grid(row=1, column=0, padx=10)

# Size Listbox
font_size_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=20 )
font_size_listbox.grid(row=1, column=1)

# Style Listbox
font_style_listbox = Listbox(bottom_frame, selectmode=SINGLE, width=20 )
font_style_listbox.grid(row=1, column=2, padx=10)

# Add Font Families To Listbox
for font in font.families():
	my_listbox.insert('end', font)

# Add Sizes To Size Listbox
font_sizes = [8, 10, 12, 14, 16, 20, 36, 48, 72]
for size in font_sizes:
	font_size_listbox.insert('end', size)

# Add Styles To Style Listbox
font_styles = ["Regular", "Bold", "Italic", "Underline"]
for style in font_styles:
	font_style_listbox.insert('end', style)	

# Bind The Listbox
my_listbox.bind('<ButtonRelease-1>', font_chooser)
font_size_listbox.bind('<ButtonRelease-1>', font_size_chooser)
font_style_listbox.bind('<ButtonRelease-1>', font_style_chooser)

def find_and_replace():
    # Get the find and replace words from the user
    find_word = find_entry.get()
    replace_word = replace_entry.get()
    start = my_text.get("1.0", "end").find(find_word)
    end = start + len(find_word)
    my_text.delete(f"1.0 + {start} chars", f"1.0 + {end} chars")
    my_text.insert(f"1.0 + {start} chars", replace_word)

    # Get the text from the widget
    text = my_text.get("1.0", "end")
    
    # Check if the find word is present in the text
    if find_word in text:
        # Replace all occurrences of the find word with the replace word
        text = text.replace(find_word, replace_word)
        
        # Set the text back to the widget
        my_text.delete("1.0", "end")
        my_text.insert("1.0", text)
        
        # Clear the find and replace entries
        find_entry.delete(0, END)
        replace_entry.delete(0, END)
    else:
        # Show an error message if the find word is not present
        messagebox.showerror("Error", "The find word is not present in the text")
	
# Add Find and Replace button
find_button = Button(bottom_frame, text="Find and Replace", command=find_and_replace)
find_button.grid(row=2, column=0, padx=10, pady=10)

# Add Find and Replace entry boxes
find_entry = Entry(bottom_frame)
find_entry.grid(row=2, column=1, padx=10, pady=10)

replace_entry = Entry(bottom_frame)
replace_entry.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()

