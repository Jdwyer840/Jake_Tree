


class WidgetUtilities:
    pass


class TreeCtrlUtilities:

    @staticmethod
    def update_tree_item_data(tree, item, key, value):
        item_data = tree.GetItemData(item)
        item_data[key] = value
        tree.SetItemData(item, item_data)