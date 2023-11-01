import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        # Create a panel to host the controls
        self.panel = wx.Panel(self)

        # Create a read-only, multi-line text control
        self.text_ctrl = wx.TextCtrl(self.panel, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_RICH2, size=(360, 220), pos=(10, 10))

        # Set some sample text (like Git changes)
        sample_text = """File: example.txt
--------------------
- This is a removed line.
+ This is an added line.

File: another_example.txt
--------------------
- Old content.
+ New content."""

        self.text_ctrl.SetValue(sample_text)

        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Read-Only wx.TextCtrl Example")
    app.MainLoop()