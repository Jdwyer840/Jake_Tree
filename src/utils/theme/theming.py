from .themes import LIGHT_THEME, DARK_THEME
import wx


class ThemeManager:

    # @staticmethod
    # def toggle_theme(theme):

    @staticmethod
    def apply_theme(widget, theme):
        # Base colors
        widget.SetBackgroundColour(wx.Colour(theme['bg']))
        widget.SetForegroundColour(wx.Colour(theme['fg']))

        # Special handling for specific widget types
        if isinstance(widget, wx.Button):
            widget.SetBackgroundColour(wx.Colour(theme['button']['bg']))
            widget.SetForegroundColour(wx.Colour(theme['button']['fg']))

        # Recursively apply theme to children
        for child in widget.GetChildren():
            ThemeManager.apply_theme(child, theme)
