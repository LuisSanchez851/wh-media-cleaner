import subprocess


class ADBClient:

    def run(self, command):

        full_command = ["adb", "shell", command]

        result = subprocess.run(
            full_command,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("ADB ERROR:", result.stderr)

        return result.stdout.strip()