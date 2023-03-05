import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, server_process):
        self.server_process = server_process

    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.event_type in ['modified', 'created']:
            print(f'Reloading server at {time.time()}')
            self.server_process.kill()
            self.server_process.wait()
            self.server_process = subprocess.Popen([sys.executable, 'arso-vreme-main.py'])

if __name__ == '__main__':
    import subprocess

    # Start the server process
    server_process = subprocess.Popen([sys.executable, 'arso-vreme-main.py'])

    # Start the watchdog observer
    event_handler = ReloadHandler(server_process)
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
