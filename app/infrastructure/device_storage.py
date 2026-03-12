from .adb_client import ADBClient
from app.domain.file import MediaFile

RUTA_BASE = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images"


class DeviceStorage:

    def __init__(self):
        self.adb = ADBClient()

    def list_files(self):

        command = f'ls "{RUTA_BASE}"'

        output = self.adb.run(command)

        files = output.split("\n")

        return [
            MediaFile(name=f.strip(), size=0, path=RUTA_BASE)
            for f in files if f.strip()
        ]

    def delete_file(self, file):

        command = f'rm "{RUTA_BASE}/{file.name}"'

        self.adb.run(command)