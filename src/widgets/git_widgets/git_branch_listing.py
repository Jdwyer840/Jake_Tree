import wx

from src.controllers.git.git_operations import GitOperations
from src.utils.theme.theming import ThemeManager
from src.utils.common.widgets import TreeCtrlUtilities


class BranchListingConstants:
    CURRENT_BRANCH = "current_branch"


class BranchListingTree(wx.TreeCtrl):

    current_branch_tree_item = None

    def __init__(self, parent):
        super(BranchListingTree, self).__init__(parent, style=wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_HIDE_ROOT | wx.TR_HAS_BUTTONS | wx.TR_EDIT_LABELS)
        git_ops = GitOperations(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
        grouped_branches = git_ops.get_branches_grouped_by_prefix_dict()

        # self.SetBackgroundColour('red')
        font = self.GetFont()
        font.SetPointSize(10)  # Set the font size to 12 points
        self.SetFont(font)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.on_item_activate_change_branch)

        hidden_root = self.AddRoot("Actual Hidden Root")

        for prefix, branch_list in grouped_branches.items():
            branch_with_prefix_root = None
            for branch in branch_list:
                if prefix == 'no_prefix':
                    self.build_git_branch_tree_item(root=hidden_root, branch_name=branch)
                else:
                    branch_with_prefix_root = self.AppendItem(hidden_root, f"{prefix}") if not branch_with_prefix_root else branch_with_prefix_root
                    self.build_git_branch_tree_item(root=branch_with_prefix_root, branch_name=branch, data={"branch": f"{prefix}/{branch}"})

        self.ExpandAll()
        self.Refresh()

    def on_item_activate_change_branch(self, event):
        select_tree_item = event.GetItem()
        if self.current_branch_tree_item == select_tree_item:
            print("trying to checkout same branch")
            return
        previous_item = self.current_branch_tree_item
        # previous_item_data = self.GetItemData(previous_item)
        select_tree_item_data = self.GetItemData(select_tree_item)
        TreeCtrlUtilities.update_tree_item_data(tree=self, item=previous_item, key=BranchListingConstants.CURRENT_BRANCH, value=False)
        TreeCtrlUtilities.update_tree_item_data(tree=self, item=previous_item, key=BranchListingConstants.CURRENT_BRANCH, value=True)
        branch_name = select_tree_item_data.get('branch')
        wx.MessageBox(f'You checked out branch: {branch_name}', 'Info', wx.OK | wx.ICON_INFORMATION)

        # Find a better way to handle theme changes and what not
        # doesnt make sense to go and change everything for one item's change
        GitOperations.check_out_local_branch(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal', branch_name)
        ThemeManager.reset_theme_style_for_widget(self)
        self.SetItemBackgroundColour(select_tree_item, wx.Colour(50, 100, 50))

    def build_git_branch_tree_item(self, root, branch_name: str, data: dict = None):
        tree_item = self.AppendItem(root, f"{branch_name}")
        if data is None:
            data = {"branch": branch_name}
        if self.is_branch_checked_out(branch_name):
            self.current_branch_tree_item = tree_item
            data["current_branch"] = True
            self.SelectItem(tree_item)
            self.highlight_current_branch(tree_item=tree_item)
        self.SetItemData(tree_item, data=data)
        self.Refresh()

    def highlight_current_branch(self, tree_item):
        self.SetItemBackgroundColour(tree_item, wx.Colour(50, 50, 50))

    @staticmethod
    def is_branch_checked_out(branch_name: str):
        current_checked_out_branch = GitOperations.get_current_branch_name()
        return branch_name == current_checked_out_branch or branch_name in current_checked_out_branch
