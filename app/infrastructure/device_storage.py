from .adb_client import ADBClient
from app.domain.file import MediaFile

RUTA_BASE = "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images"

class DeviceStorage:

    def __init__(self):
        self.adb = ADBClient()

    def list_files(self):

        ruta = RUTA_BASE.replace(" ", "\\ ")

        output = self.adb.run(["ls", ruta])

        files = output.split("\n")

        print("ADB output:", output)

        return [
            MediaFile(name=f.strip(), size=0, path=RUTA_BASE)
            for f in files if f.strip()
        ]

    def delete_file(self, file):

        ruta = RUTA_BASE.replace(" ", "\\ ")

        self.adb.run(["rm", f"{ruta}/{file.name}"])