import pyautogui

# This class is for cliquing on the screen with the mouse and coping the inofrmation of the hand review of pokerstars
class Clicker:

    def __init__(self):
        pass

    def main_loop(self):
        pass

    @staticmethod
    def click(x, y):
        pyautogui.click(x, y)

    @staticmethod
    def press_down_arrow():
        pyautogui.press('down')

    @staticmethod
    def press_ctrl_a():
        pyautogui.hotkey('ctrl', 'a')

    @staticmethod
    def press_ctrl_c():
        pyautogui.hotkey('ctrl', 'c')

    