import wx

from src.controllers.git.git_operations import GitOperations
from src.utils.theme.theming import ThemeManager
from src.widgets.git_widgets.git_branch_listing import BranchListingTree


# git branches side bar?
class Sidebar(wx.Panel):
    def __init__(self, parent):
        super(Sidebar, self).__init__(parent)
        git_ops = GitOperations(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
        grouped_branches = git_ops.get_branches_grouped_by_prefix_dict()

        self.parent_panel = parent

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # tree should be a part of this panel and not the parents thus the self here
        self.tree = BranchListingTree(self)

        self.sizer.Add(self.tree, 1, wx.EXPAND)
        # self.panel.SetSizer(self.sizer)
        self.SetSizer(self.sizer)
        self.Layout()  # Layout the sizer
