# Arda Mavi
import pyautogui
import webbrowser

def open_game(browser, url):
    return webbrowser.get(browser).open(url)

def press():
    pyautogui.keyDown('space')

def release():
    pyautogui.keyUp('space')
