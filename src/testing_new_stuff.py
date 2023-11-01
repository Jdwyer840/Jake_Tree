# import wx
# import matplotlib.pyplot as plt
# import networkx as nx
# from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# from matplotlib.collections import PathCollection
# from controllers.git.git_operations import GitOperations
#
#
# # the following code shows a gaph and if nodes are clicked an on click is triggered
# class GraphPanel(wx.Panel):
#     def __init__(self, parent):
#         super(GraphPanel, self).__init__(parent)
#
#         # Create a graph using networkx
#         self.G = nx.Graph()
#         self.G.add_node()
#         self.G.add_edge('A', 'B')
#         self.G.add_edge('B', 'C')
#
#         # Create a matplotlib figure
#         self.figure, self.ax = plt.subplots(figsize=(1, 1))
#         self.pos = nx.spring_layout(self.G)  # Positioning of nodes
#         nodes = nx.draw_networkx_nodes(self.G, pos=self.pos, ax=self.ax)
#         nx.draw_networkx_edges(self.G, pos=self.pos, ax=self.ax)
#         nx.draw_networkx_labels(self.G, pos=self.pos, ax=self.ax)
#
#         nodes.set_picker(True)  # Set picker attribute for nodes
#
#         # Embed the figure in the wxPython panel
#         self.canvas = FigureCanvas(self, -1, self.figure)
#         self.sizer = wx.BoxSizer(wx.VERTICAL)
#         self.sizer.Add(self.canvas, 1, wx.EXPAND)
#         self.SetSizer(self.sizer)
#
#         # Bind the pick event to a handler
#         self.canvas.mpl_connect('pick_event', self.on_pick)
#
#     def on_pick(self, event):
#         # Check if the pick event is on a node
#         if isinstance(event.artist, PathCollection):
#             node_index = event.ind[0]
#             node_label = list(self.G.nodes())[node_index]
#             wx.MessageBox(f"You clicked on node: {node_label}", "Info", wx.OK | wx.ICON_INFORMATION)
#
#
# class MainFrame(wx.Frame):
#     def __init__(self):
#         super(MainFrame, self).__init__(None, title="wxPython Graph Display with Node Clicks", size=(600, 500))
#         panel = GraphPanel(self)
#         self.Show()
#
#
# if __name__ == "__main__":
#     git_obj = GitOperations.get_current_remote_branches(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
#     app = wx.App(False)
#     frame = MainFrame()
#     app.MainLoop()
#
# # import networkx as nx # add to requirets if useful
# # import matplotlib.pyplot as plt
# #
# # # Create an empty graph
# # G = nx.Graph()
# #
# # # Add nodes
# # G.add_node(1)
# # G.add_node(2)
# #
# # # Add edges
# # G.add_edge(1, 2)
# #
# # # Draw the graph
# # nx.draw(G, with_labels=True)
# # plt.show()

# listctrl demo
# import wx
# import git
#
# class GitCommitPanel(wx.Panel):
#     def __init__(self, parent, repo_path):
#         super(GitCommitPanel, self).__init__(parent)
#
#         # Create ListCtrl
#         self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)
#         self.list_ctrl.InsertColumn(0, 'Commit Graph', width=200)
#         self.list_ctrl.InsertColumn(1, 'Commit Hash', width=200)
#
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(self.list_ctrl, 1, wx.EXPAND)
#         self.SetSizer(sizer)
#
#         # Populate ListCtrl with git commits
#         self.populate_list(repo_path)
#
#     def populate_list(self, repo_path):
#         repo = git.Repo(repo_path)
#         commits = list(repo.iter_commits('master', max_count=100))  # Adjust max_count as needed
#
#         for commit in commits:
#             # For simplicity, we're just using a placeholder for the commit graph.
#             # In a real-world application, you'd want to generate a visual representation of the commit graph.
#             self.list_ctrl.Append(["|", commit.hexsha])
#
#
# class MainFrame(wx.Frame):
#     def __init__(self):
#         super(MainFrame, self).__init__(None, title="Git Commits", size=(500, 400))
#         panel = GitCommitPanel(self, r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
#         self.Show()
#
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainFrame()
#     app.MainLoop()
#shows git graph
# import wx
# import git
#
# class GitGraphPanel(wx.Panel):
#     def __init__(self, parent, repo_path):
#         super(GitGraphPanel, self).__init__(parent)
#         self.repo = git.Repo(repo_path)
#         self.commits = list(self.repo.iter_commits('master', max_count=10))
#         self.Bind(wx.EVT_PAINT, self.on_paint)
#
#     def on_paint(self, event):
#         dc = wx.PaintDC(self)
#         dc.Clear()
#
#         # Starting position
#         x, y = 50, 50
#
#         # Draw each commit
#         for commit in self.commits:
#             # Draw commit circle
#             dc.DrawCircle(x, y, 10)
#
#             # Draw commit hash (or a shortened version for simplicity)
#             dc.DrawText(commit.hexsha[:7], x + 20, y - 10)
#
#             # If there's a next commit, draw a line to it
#             if self.commits.index(commit) < len(self.commits) - 1:
#                 dc.DrawLine(x, y + 10, x, y + 40)
#
#             # Move y down for the next commit
#             y += 40
#
# class MainFrame(wx.Frame):
#     def __init__(self):
#         super(MainFrame, self).__init__(None, title="Git Graph", size=(300, 500))
#         GitGraphPanel(self, r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
#         self.Show()
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainFrame()
#     app.MainLoop()

# shows git graph
# import wx
# import git
#
# class PositionedCommit:
#     def __init__(self, commit, x, y):
#         self.commit = commit
#         self.x = x
#         self.y = y
#         self.is_drawn = False
#
# class GitGraphPanel(wx.Panel):
#     def __init__(self, parent, repo_path):
#         super(GitGraphPanel, self).__init__(parent)
#         self.repo = git.Repo(repo_path)
#         self.commits = list(self.repo.iter_commits('master', max_count=20))
#         self.positioned_commits = self.position_commits()
#         self.Bind(wx.EVT_PAINT, self.on_paint)
#
#     def position_commits(self):
#         x, y = 50, 50
#         positioned_commits = []
#         for commit in self.commits:
#             positioned_commits.append(PositionedCommit(commit, x, y))
#             y += 40
#         return positioned_commits
#
#     def on_paint(self, event):
#         dc = wx.PaintDC(self)
#         dc.Clear()
#
#         for pc in self.positioned_commits:
#             if not pc.is_drawn:
#                 self.draw_commit(dc, pc)
#
#     def draw_commit(self, dc, pc):
#         # Draw commit circle
#         dc.DrawCircle(pc.x, pc.y, 10)
#
#         # Draw commit hash (or a shortened version for simplicity)
#         dc.DrawText(pc.commit.hexsha[:7], pc.x + 20, pc.y - 10)
#
#         # Draw lines to parents
#         for parent in pc.commit.parents:
#             parent_pc = next((p for p in self.positioned_commits if p.commit == parent), None)
#             if parent_pc:
#                 dc.DrawLine(pc.x, pc.y + 10, parent_pc.x, parent_pc.y - 10)
#
#         pc.is_drawn = True
#
# class MainFrame(wx.Frame):
#     def __init__(self):
#         super(MainFrame, self).__init__(None, title="Git Graph", size=(300, 500))
#         GitGraphPanel(self, r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
#         self.Show()
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainFrame()
#     app.MainLoop()

# import wx
# import git
#
# class PositionedCommit:
#     def __init__(self, commit, x, y):
#         self.commit = commit
#         self.x = x
#         self.y = y
#         self.is_drawn = False
#
# class GitGraphPanel(wx.Panel):
#     def __init__(self, parent, repo_path):
#         super(GitGraphPanel, self).__init__(parent)
#         self.repo = git.Repo(repo_path)
#         self.commits = list(self.repo.iter_commits('master', max_count=20))
#         self.develop_commits = list(self.repo.iter_commits('develop', max_count=20))
#         self.positioned_commits = self.position_commits()
#         self.Bind(wx.EVT_PAINT, self.on_paint)
#
#     def position_commits(self):
#         master_x, develop_x = 50, 150
#         y = 80
#         positioned_commits = []
#
#         # Position master commits
#         for commit in self.commits:
#             positioned_commits.append(PositionedCommit(commit, master_x, y))
#             y += 50
#
#         # Reset y for develop branch
#         y = 50
#         for commit in self.develop_commits:
#             positioned_commits.append(PositionedCommit(commit, develop_x, y))
#             y += 40
#
#         return positioned_commits
#
#     def on_paint(self, event):
#         dc = wx.PaintDC(self)
#         dc.Clear()
#
#         for pc in self.positioned_commits:
#             if not pc.is_drawn:
#                 self.draw_commit(dc, pc)
#
#     def draw_commit(self, dc, pc):
#         # Draw commit circle
#         dc.DrawCircle(pc.x, pc.y, 10)
#
#         # Draw commit hash (or a shortened version for simplicity)
#         dc.DrawText(pc.commit.hexsha[:7], pc.x + 20, pc.y - 10)
#
#         # Draw lines to parents
#         for parent in pc.commit.parents:
#             parent_pc = next((p for p in self.positioned_commits if p.commit == parent), None)
#             if parent_pc:
#                 dc.DrawLine(pc.x, pc.y + 10, parent_pc.x, parent_pc.y - 10)
#
#         pc.is_drawn = True
#
# class MainFrame(wx.Frame):
#     def __init__(self):
#         super(MainFrame, self).__init__(None, title="Git Graph", size=(400, 1000))
#         GitGraphPanel(self, r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
#         self.Show()
#
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainFrame()
#     app.MainLoop()


# from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as Canvas
# from matplotlib.backends.backend_wx import NavigationToolbar2Wx
# from matplotlib.figure import Figure
# import wx
# from wxmplot import PlotPanel
#
# class MainFrame(wx.Frame):
#     def __init__(self, parent):
#         wx.Frame.__init__(self, None, size=(1200, 900))
#         self.panel_1 = Panel_one(self)
#
# class Panel_one(wx.Panel):
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent, -1, style=wx.SUNKEN_BORDER)
#
#         # Note: here use wxmplot.PlotPanel instead of your Graph class
#         self.graph1 = PlotPanel(self, size=(400, 400))
#         self.graph2 = PlotPanel(self, size=(700, 700))
#
#         sizer = wx.BoxSizer(wx.HORIZONTAL)
#         sizer.Add(self.graph1, 0, wx.LEFT, 5)
#         sizer.Add(self.graph2, 0, wx.LEFT, 5)
#         self.SetSizer(sizer)
#
#
# class Graph(wx.Panel):
#     def __init__(self, parent,  position, size, dpi=150):
#         wx.Panel.__init__(self, parent, pos=position, size=size)
#
#         # Note: here, set the figure size based on size of Graph
#         figsize = (size[0]*1.0/dpi, size[1]*1.0/dpi)
#         self.figure = Figure(figsize, dpi=dpi)
#         self.canvas = Canvas(self, -1, self.figure)
#         self.axes = self.figure.add_subplot(111)
#
#
# if __name__ == "__main__":
#     app = wx.App(redirect=False)
#     frame = MainFrame(None)
#     frame.Show()
#     app.MainLoop()


import wx
import git  # GitPython library

repo_path = r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal'


class GitGraphPanel(wx.Panel):
    def __init__(self, parent, repo_path):
        super().__init__(parent)
        self.repo = git.Repo(repo_path)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()

        # Here, you'd draw your Git graph. For simplicity, we'll just draw circles for each commit.
        y = 10
        for commit in self.repo.iter_commits():
            dc.DrawCircle(10, y, 5)
            y += 20


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Git Graph with wxPython", size=(600, 400))

        splitter = wx.SplitterWindow(self)
        self.graph_panel = GitGraphPanel(splitter, repo_path)
        self.list_ctrl = wx.ListCtrl(splitter, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, "Commit Message")

        for commit in git.Repo(repo_path).iter_commits():
            self.list_ctrl.InsertItem(0, commit.message.split('\n')[0])

        splitter.SplitVertically(self.graph_panel, self.list_ctrl)
        splitter.SetSashGravity(0.5)
        splitter.SetMinimumPaneSize(20)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()