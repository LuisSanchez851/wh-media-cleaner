import tkinter as tk
from tkinter import ttk, messagebox

from app.infrastructure.device_storage import DeviceStorage
from app.services.scanner_service import ScannerService
from app.services.cleaner_service import CleanerService
from app.services.stats_service import StatsService
from app.domain.filters import filter_by_range
from app.interfaces.gui.components import FileList


class WhatsAppCleanerGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("WhatsApp Media Cleaner")

        self.storage = DeviceStorage()
        self.scanner = ScannerService(self.storage)
        self.cleaner = CleanerService(self.storage)
        self.stats = StatsService()

        self.files = []

        self.build_ui()

    def build_ui(self):

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Archivo desde").grid(row=0, column=0)
        self.entry_desde = ttk.Entry(frame, width=30)
        self.entry_desde.grid(row=0, column=1)

        ttk.Label(frame, text="Archivo hasta").grid(row=1, column=0)
        self.entry_hasta = ttk.Entry(frame, width=30)
        self.entry_hasta.grid(row=1, column=1)

        ttk.Button(frame, text="Escanear", command=self.scan).grid(row=2, column=0, pady=10)
        ttk.Button(frame, text="Eliminar", command=self.delete).grid(row=2, column=1)

        self.file_list = FileList(frame)
        self.file_list.grid(row=3, column=0, columnspan=2, pady=10)

        self.label_stats = ttk.Label(frame, text="")
        self.label_stats.grid(row=4, column=0, columnspan=2)

    def scan(self):

        try:

            desde = self.entry_desde.get()
            hasta = self.entry_hasta.get()

            files = self.scanner.scan()

            filtered = filter_by_range(files, desde, hasta)

            self.files = filtered

            self.file_list.set_files(filtered)

            count = self.stats.count(filtered)

            self.label_stats.config(text=f"Archivos detectados: {count}")

        except Exception as e:

            messagebox.showerror("Error", str(e))

    def delete(self):

        if not self.files:
            messagebox.showinfo("Info", "No hay archivos para eliminar")
            return

        confirm = messagebox.askyesno("Confirmar", "¿Eliminar archivos?")

        if not confirm:
            return

        deleted = self.cleaner.delete_files(self.files)

        messagebox.showinfo("Resultado", f"Archivos eliminados: {deleted}")


def start_gui():

    root = tk.Tk()
    app = WhatsAppCleanerGUI(root)
    root.mainloop()