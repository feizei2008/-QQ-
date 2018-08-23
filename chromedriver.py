import os
import pandas as pd
import codecs
from selenium import webdriver
import win32gui
from PIL import Image
import win32con, win32clipboard
from ctypes import*
os.system("getjson.py")
xd = pd.ExcelFile('out.xlsx')
df = xd.parse('Summary') #xlsx读取为pd.dataframe
df['Unnamed: 1']= df['Unnamed: 1'].apply(lambda x:str(x*100)[0:5]+"%") #改为百分比显示
print(df['Unnamed: 3'])
with codecs.open('out.html','w','utf-8') as html_file:
    html_file.write(df.to_html(header = True,index = False))
    
    
browser = webdriver.Chrome()
browser.set_window_size(600,900) #窗口大小，决定了后续网页截图的大小
browser.get("file:///C:/Users/DELL/Desktop/theme/theme/out.html")
browser.save_screenshot("shot.png")
browser.quit()

im = Image.open('C:/Users/DELL/Desktop/theme/theme/shot.png')
im.save('11.bmp')

def setImage(aString):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
    win32clipboard.CloseClipboard() 

def send_qq(to_who,msg):
    setImage(msg)
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

to_who='李四'
msg=windll.user32.LoadImageW(0, r"11.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
send_qq(to_who,msg)