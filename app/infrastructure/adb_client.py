import subprocess

class ADBClient:

    def run(self, command):

        result = subprocess.run(
            ["adb", "shell"] + command,
            capture_output=True,
            text=True
        )

        return result.stdout.strip()