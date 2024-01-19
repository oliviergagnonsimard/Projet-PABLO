import pyautogui
import time
import subprocess

class Clicker:
    """
    This class is for cliquing on the screen with the mouse and coping the inofrmation of the hand review of pokerstars
    
    Attributes:
        None

    Methods:
        _run: This function is the main function of the class, it will click on the screen and copy the hand review, it need to be in a loop so it can be used multiple times
        click: This function will click on the screen at the position given in the parameters
        press_down_arrow: This function will press the down arrow on the keyboard
        press_ctrl_a: This function will press ctrl + a on the keyboard
        press_ctrl_c: This function will press ctrl + c on the keyboard
    """

    # This function is the main function of the class, it will click on the screen and copy the hand review, it need to be in a loop so it can be used multiple times
    def _run(self, first_spot: tuple = (900,115), second_spot: tuple = (850,500)) -> str:
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
    def click(x: int, y: int) -> None:
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
    clicker = Clicker()
    time.sleep(5)
    print(clicker._run(second_spot=(850, 500)))
    pass
