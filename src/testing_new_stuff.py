import wx
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.collections import PathCollection
from controllers.git.git_operations import GitOperations


# the following code shows a gaph and if nodes are clicked an on click is triggered
class GraphPanel(wx.Panel):
    def __init__(self, parent):
        super(GraphPanel, self).__init__(parent)

        # Create a graph using networkx
        self.G = nx.Graph()
        self.G.add_edge('A', 'B')
        self.G.add_edge('B', 'C')

        # Create a matplotlib figure
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.pos = nx.spring_layout(self.G)  # Positioning of nodes
        nodes = nx.draw_networkx_nodes(self.G, pos=self.pos, ax=self.ax)
        nx.draw_networkx_edges(self.G, pos=self.pos, ax=self.ax)
        nx.draw_networkx_labels(self.G, pos=self.pos, ax=self.ax)

        nodes.set_picker(True)  # Set picker attribute for nodes

        # Embed the figure in the wxPython panel
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        # Bind the pick event to a handler
        self.canvas.mpl_connect('pick_event', self.on_pick)

    def on_pick(self, event):
        # Check if the pick event is on a node
        if isinstance(event.artist, PathCollection):
            node_index = event.ind[0]
            node_label = list(self.G.nodes())[node_index]
            wx.MessageBox(f"You clicked on node: {node_label}", "Info", wx.OK | wx.ICON_INFORMATION)

class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None, title="wxPython Graph Display with Node Clicks", size=(600, 500))
        panel = GraphPanel(self)
        self.Show()


if __name__ == "__main__":
    git_obj = GitOperations.get_current_remote_branches(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

# import networkx as nx # add to requirets if useful
# import matplotlib.pyplot as plt
#
# # Create an empty graph
# G = nx.Graph()
#
# # Add nodes
# G.add_node(1)
# G.add_node(2)
#
# # Add edges
# G.add_edge(1, 2)
#
# # Draw the graph
# nx.draw(G, with_labels=True)
# plt.show()