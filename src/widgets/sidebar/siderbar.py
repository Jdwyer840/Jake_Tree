import wx

from src.controllers.git.git_operations import GitOperations


# git branches side bar?
class Sidebar(wx.Panel):
    def __init__(self, parent):
        super(Sidebar, self).__init__(parent)
        self.parent_panel = parent
        # Create some buttons for the sidebar
        git_remote_objs = GitOperations.get_current_local_branches(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
        # Create a vertical box sizer for the sidebar
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        for branch_name, ref in git_remote_objs.items():
            btn = wx.Button(self, label=f"{branch_name}")
            btn.SetForegroundColour(wx.Colour(0, 0, 255))  # Blue text
            if GitOperations.is_branch_checked_out(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal', branch_name):
                btn.SetBackgroundColour(wx.Colour(0, 255, 255))
            else:
                btn.SetBackgroundColour(wx.Colour(255, 255, 255))
              # White background
            btn.Bind(wx.EVT_BUTTON, lambda event, r=ref: self.display_git_info(event, r)) # r is ref change this to somethin l8r
            # lambda fx_and_model_data: self._attempt_config_update_or_save(fx_and_model_data, config_model_name
            # Bind mouse events for interactivity
            btn.Bind(wx.EVT_ENTER_WINDOW, self.on_hover)
            btn.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)
            # btn.Bind(wx.EVT_BUTTON, self.on_click)
            self.sizer.Add(btn, 0, wx.EXPAND | wx.ALL, 5)

        # Set the sizer at the end of the __init__ method

        self.SetSizer(self.sizer)
        self.Layout()  # Layout the sizer

    def display_git_info(self, event,  git_obj):
        print(git_obj)
        #gtobj is branch information / ref information
        wx.MessageBox(f'You checked out branch: {git_obj.name}', 'Info', wx.OK | wx.ICON_INFORMATION)
        GitOperations.check_out_local_branch(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal', git_obj.name)
        # Change its color
        clicked_button = event.GetEventObject()
        clicked_button.SetBackgroundColour('purple')
        clicked_button.Refresh()
        #TODO helper class for changing the buttons to correct colors
    def on_hover(self, event):
        """Change button style on mouse hover."""
        btn = event.GetEventObject()
        btn.SetForegroundColour(wx.Colour(255, 0, 0))  # Change text to red
        btn.SetBackgroundColour(wx.Colour(220, 220, 220))  # Slightly grey background
        btn.Refresh()  # Refresh the button to apply changes

    def on_leave(self, event):
        """Revert button style when mouse leaves."""
        btn = event.GetEventObject()
        btn.SetForegroundColour(wx.Colour(0, 0, 255))  # Blue text
        btn.SetBackgroundColour(wx.Colour(255, 255, 255))  # White background
        btn.Refresh()

    # def on_click(self, event):
    #     """Handle button click."""
    #     wx.MessageBox("Button clicked!")
        # self.btn1 = wx.Button(self, label='Button 1')
        # self.btn2 = wx.Button(self, label='Button 2')
        # self.btn3 = wx.Button(self, label='Button 3')
        #
        # self.btn3.Bind(wx.EVT_BUTTON, self.on_button_click_create_button)
        #
        #
        #
        # # Add the buttons to the sizer
        # self.sizer.Add(self.btn1, 0, wx.EXPAND | wx.ALL, 5)
        # self.sizer.Add(self.btn2, 0, wx.EXPAND | wx.ALL, 5)
        # self.sizer.Add(self.btn3, 0, wx.EXPAND | wx.ALL, 5)

        # self.SetSizer(self.sizer)

    def on_button_click_create_button(self, event):
        # Create a new button
        new_button = wx.Button(self, label='New Button')

        # Add the new button to the main sizer
        self.sizer.Add(new_button, 0, wx.EXPAND | wx.ALL, 5)

        # Update the layout to show the new button
        self.Layout()
