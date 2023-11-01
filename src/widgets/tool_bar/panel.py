import wx

from src.controllers.git.git_operations import GitOperations


# git branches side bar?
class ToolbarPanel(wx.Panel):

    def __init__(self, parent):
        super(ToolbarPanel, self).__init__(parent)

        self.toolbar_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create a button as an example control
        self.button = wx.Button(self, label="Click Me!")
        self.toolbar_sizer.Add(self.button, 1, wx.ALIGN_LEFT)

        self.SetSizer(self.toolbar_sizer)
        self.Layout()

