import pyautogui as pg
import time

N = int(input(">> "))
#pg.click(518, 743, clicks=1, interval=0.5)
#pg.press('F11', presses=1)
pg.click(677, 16, clicks=1, interval=0.5)
#pg.moveTo(677, 16)
#pg.hotkey('winleft','printscreen')
#time.sleep(4)
for i in range(N):
    #pg.press('right', presses=1)
    time.sleep(0.4)
    pg.hotkey('winleft','printscreen')
    time.sleep(0.8)
    pg.press('pagedown', presses=1)
    pg.press('down', presses=1)

    # pg.hotkey('winleft','printscreen')
    #time.sleep(0.5)