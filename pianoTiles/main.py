import pyautogui
import win32con, win32api
import time
import keyboard


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


# To display the mousex and mousey position
# pyautogui.displayMousePosition()


# Adjust the tile cordinates accordingly
tileOne = {
    'x': 634,
    'y': 424
}
tileTwo = {
    'x': 768,
    'y': 424
}
tileThree = {
    'x': 901,
    'y': 424
}
tileFour = {
    'x': 1034,
    'y': 424
}


# Press key q to exit automation
while keyboard.is_pressed('q') == False:
    # [0], [1], [2] means R G B and 0 means color
    if pyautogui.pixel(tileOne['x'], tileOne['y'])[0] == 0:
        click(tileOne['x'], tileOne['y'])
    elif pyautogui.pixel(tileTwo['x'], tileTwo['y'])[0] == 0:
        click(tileTwo['x'], tileTwo['y'])
    elif pyautogui.pixel(tileThree['x'], tileThree['y'])[0] == 0:
        click(tileThree['x'], tileThree['y'])
    elif pyautogui.pixel(tileFour['x'], tileFour['y'])[0] == 0:
        click(tileFour['x'], tileFour['y'])
