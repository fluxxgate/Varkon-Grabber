import customtkinter
import cefpython3 as cef
import tkinter as tk
from tkinter import ttk
import platform
import threading

class BrowserFrame(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, parent)
        self.browser = None
        self.bind("<Configure>", self.on_configure)
        
        # Start CEF in a separate thread
        self.cef_thread = threading.Thread(target=self.embed_browser)
        self.cef_thread.daemon = True
        self.cef_thread.start()
    
    def embed_browser(self):
        window_info = cef.WindowInfo()
        window_info.SetAsChild(self.winfo_id(), [0, 0, 800, 600])
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(window_info, url="gui.html")
        cef.MessageLoop()
    
    def on_configure(self, event):
        if self.browser:
            self.browser.SetBounds(0, 0, event.width, event.height)

def create_tkinter_gui():
    root = tk.Tk()
    root.title("Varkon Grabber")
    root.geometry("900x700")
    
    # Create browser frame
    browser_frame = BrowserFrame(root)
    browser_frame.pack(fill=tk.BOTH, expand=True)
    
    root.mainloop()

if __name__ == '__main__':
    create_tkinter_gui()