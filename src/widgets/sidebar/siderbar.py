import wx


class Sidebar(wx.Panel):
    def __init__(self, parent):
        super(Sidebar, self).__init__(parent)
        self.parent_panel = parent
        # Create some buttons for the sidebar
        self.btn1 = wx.Button(self, label='Button 1')
        self.btn2 = wx.Button(self, label='Button 2')
        self.btn3 = wx.Button(self, label='Button 3')

        self.btn3.Bind(wx.EVT_BUTTON, self.on_button_click_create_button)

        # Create a vertical box sizer for the sidebar
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Add the buttons to the sizer
        self.sizer.Add(self.btn1, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.btn2, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.btn3, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(self.sizer)

    def on_button_click_create_button(self, event):
        # Create a new button
        new_button = wx.Button(self, label='New Button')

        # Add the new button to the main sizer
        self.sizer.Add(new_button, 0, wx.EXPAND | wx.ALL, 5)

        # Update the layout to show the new button
        self.Layout()
