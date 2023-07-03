import tkinter as tk
from threading import Thread
from tkinter import filedialog
import subprocess
import os
import sys
import json
####IMPORTANT######
######pyinstaller --onefile --add-data "Main;Main" --hidden-import pyautogui --hidden-import pydirectinput --hidden-import pyperclip --icon=Main/halo_bot_icon.ico Main/Gui.py#######
##Version1.1.8.1
###To-Do###
# Display object list size from DcJson when its selected onto the Gui
#
#
#
root = tk.Tk()

main_dir = os.path.abspath(os.path.dirname(__file__))

bot_path = os.path.join("Main", "Bot.py")

class Application(tk.Frame):
    def __init__(self, master=None):
        self.low_performance_var = tk.BooleanVar(value=False)
        self.bot_process = None
        self.stop_flag = False
        super().__init__(master)
        self.master = master
        icon_path = os.path.join("Main", "halo_bot_icon.ico")
        if os.path.exists(icon_path):
            self.master.iconbitmap(default=icon_path)

        # Set the default file path to the parent directory of the directory that contains Gui.py
        default_file_path = os.path.join(os.path.dirname(__file__), "..")
        self.file_path_var = tk.StringVar(value=default_file_path)

        self.create_widgets()

    def stop_processing(self):
        self.stop_flag = True
        if self.bot_process is not None:
            self.bot_process.terminate()
            self.bot_process = None
            self.log_to_gui("Bot process terminated.")

            # Join the thread to wait for it to finish
            if hasattr(self, "bot_output_thread") and self.bot_output_thread.is_alive():
                self.bot_output_thread.join()

    def log_to_gui(self, text):
        self.log_text.config(state="normal")
        self.log_text.insert("end", text)
        self.log_text.see("end")
        self.log_text.config(state="disabled")


    def create_widgets(self):

        json_frame = tk.Frame(self)
        json_frame.pack(side="top", fill="x", padx=100, pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(side="top",anchor="center", fill="x", padx=200, pady=5)

        options_frame = tk.Frame(self)
        options_frame.pack(side="top", fill="x", padx=275, pady=5)

        log_frame = tk.Frame(self)
        log_frame.pack(side="bottom",anchor="center", fill="x", pady=5)

        self.browse_button = tk.Button(json_frame, text="Select Json File", command=self.browse_file, width=100)
        self.browse_button.pack(side="top", expand=True, padx=100, pady=5)

        self.file_path_entry = tk.Entry(json_frame, textvariable=self.file_path_var)
        self.file_path_entry.pack(side="top", fill="x", expand=False, padx=100, pady=5)

        self.run_button = tk.Button(button_frame, text="Run Bot", command=self.run_bot, width=25, height=2, bg="green")
        self.run_button.pack(side="left", anchor="center", padx=5, pady=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_processing, bg="yellow", width=25, height=2)
        self.stop_button.pack(side="left", anchor="center", padx=5, pady=5)

        self.quit_button = tk.Button(button_frame, text="Quit", fg="red", command=self.quit_application, width=25, height=2)
        self.quit_button.pack(side="left", anchor="center", padx=5, pady=5)

        self.object_count_label = tk.Label(options_frame, text="Objects in Json file: 0")
        self.object_count_label.pack(side="top",anchor="center", padx=50, pady=10)

        self.position_only_var = tk.BooleanVar(value=False)
        self.position_only_checkbox = tk.Checkbutton(options_frame, text="Position Only", variable=self.position_only_var)
        self.position_only_checkbox.pack(side="top", anchor="center", padx=50, pady=10)

        self.low_performance_checkbox = tk.Checkbutton(options_frame, text="Low Performance (Slower Keystrokes)", variable=self.low_performance_var)
        self.low_performance_checkbox.pack(side="top", anchor="center", padx=50, pady=10)

        self.clear_button = tk.Button(log_frame, text="Clear Log", command=self.clear_log)
        self.clear_button.pack(side="top", fill="x", padx=100, pady=5)

        self.export_button = tk.Button(log_frame, text="Export Log", command=self.export_log)
        self.export_button.pack(side="top", fill="x", padx=100, pady=5)

        self.log_text = tk.Text(log_frame, state="disabled")
        self.log_text.pack(side="left", anchor="sw", fill="both", expand=True, pady=50)
    
    def clear_log(self):
        self.log_text.config(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.config(state="disabled")

    def browse_file(self):
        self.object_name_count = 0
        file_path = filedialog.askopenfilename()
        self.file_path_var.set(file_path)

        # Display object count
        if file_path:
            with open(file_path) as f:
                json_data = json.load(f)
                object_list = json_data.get('itemList', [])
                object_name_count = sum(1 for object_name in object_list if object_name.get('itemId'))
                self.object_count_label.config(text=f"Objects in Json file: {object_name_count}")


    def run_bot(self):
        path = self.file_path_var.get()
        stop_flag = bool(self.stop_flag)
        position_only = self.position_only_var.get()
        low_performance = self.low_performance_var.get()  # Get the value of the checkbox
        print(f"The value of low_performance is: {low_performance}")
        self.bot_process = subprocess.Popen(["python", bot_path, path, str(stop_flag), str(position_only), str(low_performance)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)

        # Start a thread to read the bot process output
        self.bot_output_thread = Thread(target=self.read_bot_output)
        self.bot_output_thread.start()

    def read_bot_output(self):
        with self.bot_process.stdout:
            for line in iter(self.bot_process.stdout.readline, b''):
                self.log_to_gui(line.decode())
                sys.stdout.flush()  # Flush the standard output

    def quit_application(self):
        self.stop_processing()
        self.master.destroy()

#    def execute_bot(self, path, stop_flag):
#        bot_process = subprocess.Popen(["python", bot_path, path, str(stop_flag)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
#
#        with bot_process.stdout:
#            for line in iter(bot_process.stdout.readline, b''):
#                self.log_to_gui(line.decode())
#                sys.stdout.flush()  # Flush the standard output

    def export_log(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.log_text.get("1.0", "end"))


root.title("TubbyMcFatDuck's Halo Bot v1.1.8.1")  # Set the title of the application window
app = Application(master=root)
app.pack(fill="both", expand=True)
root.geometry("1000x750")
root.wm_minsize(500, 500)  # Set a minimum size for the window
app.mainloop()
