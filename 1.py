import win32api, win32gui, win32con
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import cv2

from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 只能是绝对路径
a = 'E:\\zhuomian\\1.jpg'
temp = 'temp'+os.path.split(a)[1]
temp = os.path.join(os.path.split(a)[0], temp)



img = cv2.imread(a)[:,:,::-1]

def change_cv2_draw(image,strs,local, where, colour=(255, 0, 0), sizes=30):
    # 转换图片
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # 读入图片
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    # 字体
    font = ImageFont.truetype("YunShuFaJiaYangYongZhiShouJinZhengKaiJian-2.ttf", sizes, encoding="utf-8")
    draw.text(local, strs, colour, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

    return image

a = change_cv2_draw(img, '2020.5.6 计划:', (1000,300), temp)
a = change_cv2_draw(a, '  1.PDE的论文和佐治亚',   (1000,330), temp)
a = change_cv2_draw(a, '√  2.张宇高数 P24',   (1000,360), temp)
a = change_cv2_draw(a, '学如逆水行舟不进则退', (800, 800), temp, colour=(255, 255, 0), sizes=50)


mpimg.imsave(temp, a)

##############################
def setWallPaper(pic):
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0 , win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, win32con.SPIF_SENDWININICHANGE)




setWallPaper(temp)