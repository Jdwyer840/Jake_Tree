import wx

from src.utils.theme.themes import DARK_THEME, LIGHT_THEME
from src.utils.theme.theming import ThemeManager
from src.widgets.sidebar.siderbar import Sidebar

from src.controllers.git.git_operations import GitOperations


class ApplicationThemeCodes:
    DARK_THEME = 'DARK'
    LIGHT_THEME = 'LIGHT'


class AppFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(AppFrame, self).__init__(*args, **kw)
        self.theme = ApplicationThemeCodes.LIGHT_THEME


        # Create a panel to host the controls
        self.panel = wx.Panel(self)

        # Create a text control (text input)
        self.text_ctrl = wx.TextCtrl(self.panel)

        # Create a button
        self.display_text_button = wx.Button(self.panel, label='Display Text!')
        self.display_text_button.Bind(wx.EVT_BUTTON, self.on_button_click)

        self.toggle_theme_button = wx.Button(self.panel, label='Dark Mode!')
        self.toggle_theme_button.Bind(wx.EVT_BUTTON, self.on_click_theme_toggle)

        # Create the sidebar
        self.sidebar = Sidebar(self.panel)

        # Set up the main sizer
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.sidebar, 1, wx.EXPAND | wx.ALL, 5)  # Sidebar takes up 1 part of the horizontal space
        main_sizer.Add(self.text_ctrl, 3, wx.EXPAND | wx.ALL, 5)  # Text control takes up 3 parts
        main_sizer.Add(self.display_text_button, 1, wx.ALL, 5)  # Button takes up 1 part
        main_sizer.Add(self.toggle_theme_button, 1, wx.ALL, 5)  # Button takes up 1 part

        self.panel.SetSizer(main_sizer)

    def on_click_theme_toggle(self, event):
        # TODO move this code to theme module
        if self.theme == ApplicationThemeCodes.LIGHT_THEME:
            ThemeManager.apply_theme(self.panel, DARK_THEME)
            self.theme = ApplicationThemeCodes.DARK_THEME
            self.toggle_theme_button.SetLabel("Light Mode")
            # self.panel.SetBackgroundColour(wx.Colour(50, 50, 50))
        else:
            ThemeManager.apply_theme(self.panel, LIGHT_THEME)
            self.theme = ApplicationThemeCodes.LIGHT_THEME
            self.toggle_theme_button.SetLabel("Dark Mode")
            # self.panel.SetBackgroundColour(wx.Colour(123, 58, 230))
        self.panel.Refresh()
        # self.panel.()

    def on_button_click(self, event):
        user_input = self.text_ctrl.GetValue()
        wx.MessageBox(f'You entered: {user_input}', 'Info', wx.OK | wx.ICON_INFORMATION)
