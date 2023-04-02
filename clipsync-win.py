import requests
import time
import pyperclip
import pystray
import threading
from PIL import Image

def send_clipboard_to_server(content):
    try:
        payload = {"platform": "windows", "content": content}
        response = requests.post("http://yourip:8000/clipboard", data=payload)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return {}
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return {}

def get_clipboard_from_server():
    try:
        response = requests.get("http://yourip:8000/clipboard?platform=ios")
        return response.json().get("content", "")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return ""
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return ""

def check_for_clipboard_changes():
    previous_ios_clipboard = ""
    while True:
        time.sleep(1)
        ios_clipboard = get_clipboard_from_server()
        if ios_clipboard != previous_ios_clipboard:
            previous_ios_clipboard = ios_clipboard
            current_windows_clipboard = pyperclip.paste()
            send_clipboard_to_server(current_windows_clipboard)
            pyperclip.copy(ios_clipboard)

def on_quit(icon, item):
    icon.stop()

def minimize_to_tray(icon):
    icon.visible = True

    menu = (pystray.MenuItem('退出', on_quit),)
    icon.menu = pystray.Menu(*menu)

    t = threading.Thread(target=check_for_clipboard_changes)
    t.daemon = True
    t.start()

if __name__ == '__main__':
    image = Image.open("icon.png") # 请提供一个名为 "icon.png" 的图标文件
    icon = pystray.Icon("clipboard_sync", image, "Clipboard Sync")
    icon.run(minimize_to_tray)
