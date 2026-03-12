import tkinter as tk
from tkinter import ttk


class FileList(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.listbox = tk.Listbox(self, width=80, height=20)
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.listbox.yview)

        self.listbox.configure(yscrollcommand=self.scroll.set)

        self.listbox.pack(side="left", fill="both", expand=True)
        self.scroll.pack(side="right", fill="y")

    def set_files(self, files):

        self.listbox.delete(0, tk.END)

        for f in files:
            self.listbox.insert(tk.END, f.name)

    def get_selected(self):

        return self.listbox.get(0, tk.END)