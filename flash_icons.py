#encoding:utf-8
''' Flash windows tray icon sample code '''

from Tkinter import Tk, Menu
import tkMessageBox
import os
import time
import threading

icon_state = False    # Show icon0 when False, else show icon1 
def flash_icon():
    global icon_state
    while True:
        root.tk.call('winico', 'taskbar', 'modify', icon,
                     '-pos', int(not icon_state), '-text', u'Flash Icon APP')
        icon_state = not icon_state
        time.sleep(0.5)

def menu_func(event, x, y):
    if event == 'WM_RBUTTONDOWN':    # Right click tray icon, pop up menu
        menu.tk_popup(x, y)

def say_hello():
    tkMessageBox.showinfo('msg', 'you clicked say hello button.')


root = Tk()
root.tk.call('package', 'require', 'Winico')
icon = root.tk.call('winico', 'createfrom', os.path.join(os.getcwd(), 'test.ico'))    # New icon resources
root.tk.call('winico', 'taskbar', 'add', icon,
             '-callback', (root.register(menu_func), '%m', '%x', '%y'),
             '-pos',0,
             '-text',u'Flash Icon APP')
menu = Menu(root, tearoff=0)
menu.add_command(label='Say Hello', command=say_hello)
menu.add_command(label='Quit', command=root.quit)

t = threading.Thread(target=flash_icon)    # Create a new thread
t.setDaemon(True)
t.start()

root.withdraw()
root.mainloop()