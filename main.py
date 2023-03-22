###############################################
# RANDOM PASSWORD GENERATOR [v1.0 13-03-2023] #
###############################################

#Import necessary modules
import tkinter as tk
import tkinter.messagebox as msgbox
import pyperclip, random, string
from tkinter import filedialog
from tooltip import Tooltip


class PasswordGeneratorApp(tk.Frame):
    """Creates a class for the app."""
    def __init__(self, master=None):
        """Initiate the app."""
        super().__init__(master)
        self.master = master
        #Set up a font
        self.font = ("TkDefaultFont", 12, "bold")
        #Create widgets
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets. Pretty self-explainatory."""
        #Password length label and entry widget
        self.length_label = tk.Label(self.master, text="Password Length:", font=self.font)
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.length_entry = tk.Entry(self.master, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.length_entry.tip = Tooltip(self.length_entry, "Add the desired length for your password here. Make sure it is a valid number.")
        self.length_entry.insert(0, "12")

        #Password characters label and entry widget
        self.undesired_characters_label = tk.Label(self.master, text="Not desired characters:", font=self.font)
        self.undesired_characters_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.undesired_characters_entry = tk.Entry(self.master, width=30)
        self.undesired_characters_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.undesired_characters_entry.tip = Tooltip(self.undesired_characters_entry, "Add characters you don't want in you password to appear. Remember this field is case sensitive.")

        #Password strength label and radio buttons
        self.strength_label = tk.Label(self.master, text="Password Strength:", font=self.font)
        self.strength_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.strength_var = tk.StringVar(value="2")
        self.weak_radio = tk.Radiobutton(self.master, text="Weak (only letters)", variable=self.strength_var, value="1")
        self.weak_radio.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.medium_radio = tk.Radiobutton(self.master, text="Medium (letters and numbers)", variable=self.strength_var, value="2")
        self.medium_radio.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.strong_radio = tk.Radiobutton(self.master, text="Strong (letters, numbers, and symbols)", variable=self.strength_var, value="3")
        self.strong_radio.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        #Generate password button
        self.generate_button = tk.Button(self.master, text="Generate Password", relief="flat", background="grey75", width=20, height=3, command=self.generate_password)
        self.generate_button.grid(row=4, column=1, columnspan=2, padx=0, pady=10, sticky="new")
        self.copy_button = tk.Button(self.master, text="Copy Password", relief="flat", background="grey75", command=self.copy_password)
        self.copy_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)
        self.save_button = tk.Button(self.master, text="Save Password", relief="flat", background="grey74", command=self.save_as)
        self.save_button.grid(row=7, column=1, columnspan=2, padx=5, pady=10)

        #Password display label and text widget
        self.password_label = tk.Label(self.master, text="Your Password:", font=self.font)
        self.password_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.password_text = tk.Text(self.master, height=1, width=self.length_entry.get())
        self.password_text.grid(row=6, column=1, padx=0, pady=10, sticky="w")

    def generate_password(self):
        """Generate a random password according to the desired settings."""
        #Get password length from entry widget
        length = self.length_entry.get()
        try:
            length = int(length)
            if length <= 0 or length > 40:
                msgbox.showerror(title="Error", message="Password length must be between 1 and 40!")
                return "InvalidLength"
            self.password_text.configure(width=length)
        except ValueError:
            msgbox.showerror(title="Error", message="Password length must be a positive integer!")
            return "InvalidLength"

        #Get password strength from radio buttons
        strength = int(self.strength_var.get())
        not_desired_characters = set(self.undesired_characters_entry.get())

        #Generate password based on strength
        if strength == 1:
            #Only letters
            available_chars = set(string.ascii_letters) - not_desired_characters
            self.password = "".join(random.choice(list(available_chars)) for _ in range(length))
        elif strength == 2:
            #Letters and numbers
            available_chars = set(string.ascii_letters + string.digits) - not_desired_characters
            self.password = ''.join(random.choice(list(available_chars)) for _ in range(length))
        else:
            #Letters, numbers, and symbols
            available_chars = set(string.ascii_letters + string.digits + string.punctuation) - not_desired_characters
            self.password = ''.join(random.choice(list(available_chars)) for _ in range(length))

        #Display password in text widget
        self.password_text.delete("1.0", tk.END)
        self.password_text.insert("1.0", self.password)
    
    def copy_password(self):
        """Copy the password to the user's clipboard."""
        password = self.password_text.get("1.0", tk.END).strip()
        if password and not password.isspace():
            pyperclip.copy(password)
        else:
            return "NoTextToCopy"
    
    def save_as(self):
        """Save the password to a file."""
        #Get the password
        password = self.password_text.get("1.0", tk.END)
        #Prompt the user for a file name and directory
        file_path = filedialog.asksaveasfilename(
            initialdir="~/Desktop",
            initialfile="password.txt",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        file_name = file_path.split("/")[-1]
        #Save the password to the selected file
        if file_path:
            text = f"Password: {password}"
            with open(file_path, "w") as file:
                file.write(text)
            msgbox.showinfo(title="Success", message=f"Password saved successfully as {file_name}!")

#Create and run the application
WIDTH, HEIGHT = 600, 370
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}+{root.winfo_screenwidth()//2 - WIDTH // 2}+{root.winfo_screenheight()//2 - HEIGHT // 2}")
root.title("Random Password Generator")
root.iconbitmap("icon.ico")
app = PasswordGeneratorApp(master=root)
app.mainloop()