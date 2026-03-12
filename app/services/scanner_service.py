class ScannerService:

    def __init__(self, storage):
        self.storage = storage

    def scan(self):
        return self.storage.list_files()