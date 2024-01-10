import pyautogui
import time
import subprocess
# This class is for cliquing on the screen with the mouse and copying the information of the hand review of pokerstars
class Clicker:

    def __init__(self):
        pass

    def _run(self, first_spot: tuple = (900,115), second_spot: tuple = (850,500)) -> None:
        self.click(first_spot[0], first_spot[1])
        time.sleep(0.5)
        self.press_down_arrow()
        time.sleep(0.5)
        self.click(second_spot[0], second_spot[1])
        time.sleep(0.5)
        self.press_ctrl_a()
        time.sleep(0.5)
        self.press_ctrl_c()
        time.sleep(0.5)
        return subprocess.check_output('powershell Get-Clipboard', shell=True).decode('utf-8') # take wahat is in the clipboard so it is the hand review
    
    @staticmethod
    def click(x, y) -> None:
        pyautogui.click(x, y)

    @staticmethod
    def press_down_arrow() -> None:
        pyautogui.press('down')

    @staticmethod
    def press_ctrl_a() -> None:
        pyautogui.hotkey('ctrl', 'a')

    @staticmethod
    def press_ctrl_c() -> None:
        pyautogui.hotkey('ctrl', 'c')


    
if __name__ == '__main__':
    #pyautogui.displayMousePosition()
    #clicker = Clicker()
    #time.sleep(5)
    #print(clicker._run())
    pass
    