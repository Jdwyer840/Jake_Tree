import wx

from widgets.sidebar.siderbar import Sidebar


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Create a panel to host the controls
        self.panel = wx.Panel(self)

        # Create a text control (text input)
        self.text_ctrl = wx.TextCtrl(self.panel)

        # Create a button
        self.button = wx.Button(self.panel, label='Click Me!')
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)

        # Create the sidebar
        self.sidebar = Sidebar(self.panel)

        # Set up the main sizer
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.sidebar, 1, wx.EXPAND | wx.ALL, 5)  # Sidebar takes up 1 part of the horizontal space
        main_sizer.Add(self.text_ctrl, 3, wx.EXPAND | wx.ALL, 5)  # Text control takes up 3 parts
        main_sizer.Add(self.button, 1, wx.ALL, 5)  # Button takes up 1 part

        self.panel.SetSizer(main_sizer)

    def on_button_click(self, event):
        user_input = self.text_ctrl.GetValue()
        wx.MessageBox(f'You entered: {user_input}', 'Info', wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None, title="wxPython Example", size=(1500, 1850))
    frame.Show()
    app.MainLoop()