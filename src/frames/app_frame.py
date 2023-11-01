import wx

from src.utils.theme.themes import DARK_THEME, LIGHT_THEME
from src.utils.theme.theming import ThemeManager
from src.widgets.git_widgets.sidebar import Sidebar
# from src.widgets.sidebar.siderbar import Sidebar
from src.widgets.git_widgets.git_graph_panel import GitGraphPanel
from src.controllers.git.git_operations import GitOperations
from src.widgets.tool_bar.panel import ToolbarPanel
from src.config.config_manager import ConfigManager

class ApplicationThemeCodes:
    DARK_THEME = 'DARK'
    LIGHT_THEME = 'LIGHT'


class AppFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(AppFrame, self).__init__(*args, **kw)
        self.theme = ConfigManager.get_config('theme_config')['theme'].upper()

        # Create a panel to host the controls
        self.panel = wx.Panel(self)

        self.toggle_theme_button = wx.Button(self.panel, label='Dark Mode!')
        self.toggle_theme_button.Bind(wx.EVT_BUTTON, self.on_click_theme_toggle)

        # Create the sidebar, graph, and toolbar
        self.sidebar = Sidebar(self.panel)
        self.graph = GitGraphPanel(self.panel)
        self.toolbar = ToolbarPanel(self.panel)

        # Set up the main sizer (vertical)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add the toolbar to the main sizer
        main_sizer.Add(self.toolbar, 0, wx.ALIGN_LEFT | wx.ALL, 3)

        # Create a horizontal sizer for the content
        content_sizer = wx.BoxSizer(wx.HORIZONTAL)
        content_sizer.Add(self.sidebar, 1, wx.EXPAND | wx.ALL, 5)
        content_sizer.Add(self.graph, 2, wx.EXPAND | wx.ALL, 1)
        content_sizer.Add(self.toggle_theme_button, 0, wx.ALL, 5)

        # Add the content sizer to the main sizer
        main_sizer.Add(content_sizer, 1, wx.EXPAND)

        self.panel.SetSizer(main_sizer)
        self.load_application_theme()

    def load_application_theme(self):
        theme_obj = ThemeManager.get_theme_object(self.theme)
        ThemeManager.apply_theme(self.panel, theme_obj)
        self.toggle_theme_button.SetLabel(f"Dark Mode" if self.theme.upper() == ApplicationThemeCodes.LIGHT_THEME else "Light Mode")
        self.panel.Refresh()

    def toggle_theme(self):
        if self.theme == ApplicationThemeCodes.LIGHT_THEME:
            ConfigManager.set_config('theme_config', 'theme', ApplicationThemeCodes.DARK_THEME)
            ThemeManager.apply_theme(self.panel, DARK_THEME)
            self.theme = ApplicationThemeCodes.DARK_THEME
            self.toggle_theme_button.SetLabel("Light Mode")
            # self.panel.SetBackgroundColour(wx.Colour(50, 50, 50))
        else:
            ConfigManager.set_config('theme_config', 'theme', ApplicationThemeCodes.LIGHT_THEME)
            ThemeManager.apply_theme(self.panel, LIGHT_THEME)
            self.theme = ApplicationThemeCodes.LIGHT_THEME
            self.toggle_theme_button.SetLabel("Dark Mode")
        self.panel.Refresh()

    def on_click_theme_toggle(self, event):
        # TODO move this code to theme module... maybe
        self.toggle_theme()

