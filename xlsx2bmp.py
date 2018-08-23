import os
import win32gui
from PIL import Image
import win32con, win32clipboard
from PIL import ImageGrab   #用于获取复制的图片
import win32com.client as win32 # 打开excel文件
from ctypes import*

os.system("getjson.py") #此脚本运行生成out.xlsx文件
path = 'C:\\Users\\DELL\\Desktop\\theme\\theme\\'
excel = win32.Dispatch('Excel.Application') #获取Excel
excel.Visible = False    #进程可见，False是它暗自进行
excel.DisplayAlerts = 0   #不跳出警告  
wb = excel.Workbooks.Open(path+'out.xlsx',False) #打开文件，有时候会有警告框说由外部链接什么的（与里面公式有关），要点是则True，否则False
ws = wb.Worksheets('Summary')        # 获取Sheet“Summary”

ws.Range('A1:D24').CopyPicture()    # 复制A1:D24图片区域
ws.Paste(ws.Range('K1'))    # 将图片移动到K1
ws.Shapes('Picture 1').Copy()    # 复制移动的图片Picture 1
img = ImageGrab.grabclipboard()  # 获取图片数据
img.save(path+'Picture 1.png') # 图片另存为
wb.Close(False)    #关闭该文件，并保存。不保存就是False
excel.quit()

im = Image.open('C:/Users/DELL/Desktop/theme/theme/Picture 1.png')
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

to_who='张三' #好友/群QQ窗口须为活动状态
msg=windll.user32.LoadImageW(0, r"11.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
if msg != 0: #由于图片编码问题，图片载入失败的话，msg为0
    send_qq(to_who,msg)
