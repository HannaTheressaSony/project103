import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir ="C:/Users/hp/Downloads"

class fileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey ,{event.src_path}has been created !")
    
    def on_modified(self,event):
        print(f"woww someone modified {event.src_path}!")
    
    def on_moved(self,event):
        print(f"caution someone moved {event.src_path}!")
    
    def on_deleted(self,event):
        print(f"Oops someone deleted {event.src_path}!")
    


eventHandler=fileEventHandler()
observer=Observer()
observer.schedule(eventHandler,from_dir,recursive=True)
observer.start()
try:
  while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
   print("Stopped")
   observer.stop()
