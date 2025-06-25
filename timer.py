import threading
import time

class CountdownTimer:
    def __init__(self, hours=2):
        self.total_seconds = hours * 60 * 60
        self.remaining = self.total_seconds
        self.running = False
        self._thread = None

    def start(self):
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._run)
            self._thread.daemon = True  # So it won't block exit
            self._thread.start()

    def _run(self):
        while self.running and self.remaining > 0:
            time.sleep(1)
            self.remaining -= 1

    def stop(self):
        self.running = False

    def reset(self):
        self.stop()
        self.remaining = self.total_seconds

    def get_time(self):
        mins, secs = divmod(self.remaining, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"
