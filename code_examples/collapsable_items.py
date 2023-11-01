import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create a TreeCtrl with a hidden root
        self.tree = wx.TreeCtrl(self.panel, style=wx.TR_FULL_ROW_HIGHLIGHT | wx.TR_HIDE_ROOT)
        font = self.tree.GetFont()
        font.SetPointSize(12)  # Set the font size to 12 points
        self.tree.SetFont(font)
        hidden_root = self.tree.AddRoot("Actual Hidden Root")

        # First main item (appears as a root)
        root1 = self.tree.AppendItem(hidden_root, "Root 1")
        item1 = self.tree.AppendItem(root1, "Item 1")
        self.tree.AppendItem(item1, "Subitem 1.1")
        self.tree.AppendItem(item1, "Subitem 1.2")

        item2 = self.tree.AppendItem(root1, "Item 2")
        self.tree.AppendItem(item2, "Subitem 2.1")
        self.tree.AppendItem(item2, "Subitem 2.2")

        # Second main item (appears as a root)
        root2 = self.tree.AppendItem(hidden_root, "Root 2")
        root2_item = self.tree.AppendItem(root2, "Root 2 Item1")
        self.tree.AppendItem(root2_item, "Subitem 1.1")
        self.tree.AppendItem(root2_item, "Subitem 1.2")

        self.sizer.Add(self.tree, 1, wx.EXPAND)
        self.panel.SetSizer(self.sizer)

        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.on_item_expanded)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.on_item_collapsed)

    def on_item_expanded(self, event):
        print("Item expanded:", self.tree.GetItemText(event.GetItem()))

    def on_item_collapsed(self, event):
        print("Item collapsed:", self.tree.GetItemText(event.GetItem()))

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None, "Collapsible List with wxPython")
    frame.Show()
    app.MainLoop()