import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(400, 300))

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Create a TreeCtrl
        self.tree = wx.TreeCtrl(self.panel, style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT)

        # Create an image list and add icons
        self.image_list = wx.ImageList(16, 16)
        arrow_idx = self.image_list.Add(wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN, size=(16, 16)))
        self.tree.AssignImageList(self.image_list)

        hidden_root = self.tree.AddRoot("Hidden Root")
        visible_root = self.tree.AppendItem(hidden_root, "Visible Root")
        self.tree.SetItemImage(visible_root, arrow_idx)  # Set the arrow icon for the visible root

        # Style the visible root with an underline
        font = self.tree.GetItemFont(visible_root)
        font.SetUnderlined(True)
        self.tree.SetItemFont(visible_root, font)

        # Add some items
        item1 = self.tree.AppendItem(visible_root, "Item 1")
        self.tree.AppendItem(item1, "Subitem 1.1")
        self.tree.AppendItem(item1, "Subitem 1.2")

        item2 = self.tree.AppendItem(visible_root, "Item 2")
        self.tree.AppendItem(item2, "Subitem 2.1")
        self.tree.AppendItem(item2, "Subitem 2.2")

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
    frame = MyFrame(None, "Styled Tree with wxPython")
    frame.Show()
    app.MainLoop()