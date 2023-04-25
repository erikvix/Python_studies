import pyautogui as bot
bot.PAUSE = 2
bot.hotkey('alt', 'tab')
bot.click(x=18, y=286)
bot.click(x=658, y=856)
bot.write('ola')
bot.press('enter')
# print(bot.position())
