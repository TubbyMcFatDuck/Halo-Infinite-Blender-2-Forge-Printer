import tkinter as tk
from threading import Thread
from tkinter import filedialog
import subprocess
import os
####IMPORTANT######
######pyinstaller --onefile --add-data "Main;Main" --icon=Main/halo_bot_icon.ico Main/Gui.py#######
root = tk.Tk()

main_dir = os.path.abspath(os.path.dirname(__file__))

bot_path = os.path.join("Main", "Bot.py")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        icon_path = os.path.join("Main", "halo_bot_icon.ico")
        if os.path.exists(icon_path):
            self.master.iconbitmap(default=icon_path)

        # Set the default file path to the parent directory of the directory that contains Gui.py
        default_file_path = os.path.join(os.path.dirname(__file__), "..")
        self.file_path_var = tk.StringVar(value=default_file_path)

        self.create_widgets()

    # ...

    def create_widgets(self):

        self.browse_button = tk.Button(self, text="Select Json File", command=self.browse_file)
        self.browse_button.pack(side="top", fill="x", padx=100, pady=5)

        self.file_path_entry = tk.Entry(self, textvariable=self.file_path_var)
        self.file_path_entry.pack(side="top", fill="x", expand=False, padx=100, pady=5)

        self.run_button = tk.Button(self, text="Run Bot", command=self.run_bot)
        self.run_button.pack(side="top", fill="x", padx=100, pady=5)

        self.export_button = tk.Button(self, text="Export Log", command=self.export_log)
        self.export_button.pack(side="top", fill="x", padx=100, pady=5)

        self.quit_button = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="top", fill="x", padx=100, pady=5)

        self.log_text = tk.Text(self, state="disabled")
        self.log_text.pack(side="bottom", fill="both", expand=True)


    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path_var.set(file_path)

    def run_bot(self):
        path = self.file_path_var.get()
        bot_thread = Thread(target=self.execute_bot, args=(path,))
        bot_thread.start()

    def execute_bot(self, path):
        bot_process = subprocess.Popen(["python", bot_path, path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)

        with bot_process.stdout:
            for line in iter(bot_process.stdout.readline, b''):
                self.log_text.config(state="normal")
                self.log_text.insert("end", line.decode())
                self.log_text.see("end")
                self.log_text.config(state="disabled")

    def export_log(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.log_text.get("1.0", "end"))


root.title("TubbyMcFatDuck's Halo Bot")  # Set the title of the application window
app = Application(master=root)
app.pack(fill="both", expand=True)
root.geometry("1000x1000")
root.wm_minsize(500, 500)  # Set a minimum size for the window
app.mainloop()
