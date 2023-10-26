import wx
from frames.app_frame import AppFrame


if __name__ == '__main__':
    app = wx.App(False)
    frame = AppFrame(None, title="wxPython Example", size=(1500, 1850))
    frame.Show()
    app.MainLoop()
