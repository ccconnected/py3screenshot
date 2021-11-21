#First install wxPython: https://wiki.wxpython.org/How%20to%20install%20wxPython

import wx
from datetime import datetime
import time

time.sleep(5)

app=wx.App()
screen=wx.ScreenDC()
size=screen.GetSize()
bmp=wx.Bitmap(size[0],size[1])
mem=wx.MemoryDC(bmp)
mem.Blit(0,0,size[0],size[1], screen,0,0)
del mem

t=datetime.now()
name="screenshot_" + t.strftime("%Y") + t.strftime("%m") + t.strftime("%d") + "_" + t.strftime("%H") + t.strftime("%M") + t.strftime("%S") + ".png"
bmp.SaveFile(name, wx.BITMAP_TYPE_PNG) #output name example: screenshot_20210202_013815.png
