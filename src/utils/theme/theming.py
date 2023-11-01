from .themes import LIGHT_THEME, DARK_THEME
from src.config.config_manager import ConfigManager
import wx


class ThemeManager:

    # @staticmethod
    # def toggle_theme(theme):

    @staticmethod
    def apply_theme(widget, theme):
        # Base colors
        # this overries colors and crud, so gota work around this
        widget.SetBackgroundColour(wx.Colour(theme['bg']))
        widget.SetForegroundColour(wx.Colour(theme['fg']))

        # Special handling for specific widget types
        if isinstance(widget, wx.Button):
            widget.SetBackgroundColour(wx.Colour(theme['button']['bg']))
            widget.SetForegroundColour(wx.Colour(theme['button']['fg']))

        if isinstance(widget, wx.TreeCtrl):
            root = widget.GetRootItem()
            if root.IsOk():  # Check if the root item is valid
                ThemeManager.traverse_tree_ctrl_widget(widget, root, theme)
                return

        # Recursively apply theme to children
        for child in widget.GetChildren():
            ThemeManager.apply_theme(child, theme)

    @staticmethod
    def traverse_tree_ctrl_widget(tree, item, theme):
        child, cookie = tree.GetFirstChild(item)
        while child.IsOk():
            data = tree.GetItemData(child)
            # if data and data.get('checkedout_branch', False):
            if child != tree.GetSelection():
                tree.SetItemBackgroundColour(child, theme['bg'])
            tree.SetItemTextColour(child, theme['fg'])
            ThemeManager.traverse_tree_ctrl_widget(tree, child, theme)
            child, cookie = tree.GetNextChild(item, cookie)

    @staticmethod
    def get_theme_object(theme: str):
        # can add extra check here to ensure dark theme
        return LIGHT_THEME if theme.upper() == "LIGHT" else DARK_THEME

    @staticmethod
    def reset_theme_style_for_widget(widget):
        """Not sure if this should live here? for changing colors back after an action is performed
        that changes colors and other styles i guess"""
        theme_obj = ThemeManager.get_theme_object(ConfigManager.get_config('theme_config')['theme'])
        if isinstance(widget, wx.TreeCtrl):
            widget.SetBackgroundColour(wx.Colour(theme_obj['bg']))
            widget.SetForegroundColour(wx.Colour(theme_obj['fg']))
            root = widget.GetRootItem()
            if root.IsOk():  # Check if the root item is valid
                print("root is ok i guess")
                ThemeManager.traverse_tree_ctrl_widget(widget, root, theme_obj)
            widget.Refresh()
        else:
            ThemeManager.apply_theme(widget, theme_obj)

