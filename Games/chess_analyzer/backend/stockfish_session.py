import subprocess
import threading

class StockfishSession:
    def __init__(self, path):
        self.process = subprocess.Popen(
            [path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            universal_newlines=True,
            bufsize=1
        )
        self.lock = threading.Lock()

    def send(self, command: str):
        with self.lock:
            self.process.stdin.write(command + "\n")
            self.process.stdin.flush()

    def read_lines(self):
        while True:
            line = self.process.stdout.readline()
            if line:
                yield line.strip()