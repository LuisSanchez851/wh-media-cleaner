class CleanerService:

    def __init__(self, storage):
        self.storage = storage

    def delete_files(self, files):

        deleted = 0

        for f in files:
            self.storage.delete_file(f)
            deleted += 1

        return deleted