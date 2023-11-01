import wx
import git
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# from scipy.constants import G

from src.controllers.git.git_operations import GitOperations


class GitGraphPanel(wx.Panel):
    def __init__(self, parent):  # should have access to repo
        super().__init__(parent)

        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, 'Commit Graph', width=100)
        self.list_ctrl.InsertColumn(1, 'Commit Hash', width=200)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.EXPAND)
        self.SetSizer(sizer)

        # Populate ListCtrl with git commits
        self.populate_list()

    def populate_list(self):
        # repo = git.Repo(repo_path)
        # commits = list(repo.iter_commits('master', max_count=100))  # Adjust max_count as needed
        commits = GitOperations.get_commit_history(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
        for commit in commits:
            # For simplicity, we're just using a placeholder for the commit graph.
            # In a real-world application, you'd want to generate a visual representation of the commit graph.
            self.list_ctrl.Append(["|", commit.hexsha])





        # # Create the graph
        # self.graph = nx.DiGraph()
        # self.repo = git.Repo(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
        #
        # x = GitOperations.get_commit_history(r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal')
        #
        # positions = {}  # Dictionary to store positions of nodes
        # label_positions = {}  # Dictionary to store positions of labels
        # y_position = 0
        # for commit in x:
        #     self.graph.add_node(commit.hexsha)  # Add commit as a node
        #     positions[commit.hexsha] = (-1, y_position)  # X remains 0, Y decreases
        #     label_positions[commit.hexsha] = (0, y_position)  # X is shifted to the right for labels
        #     y_position -= 20  # Increase the decrement to space out nodes more
        #
        #     for parent in commit.parents:
        #         self.graph.add_edge(commit.hexsha, parent.hexsha)
        #         if parent.hexsha not in positions:
        #             positions[parent.hexsha] = (-1, y_position)
        #             label_positions[parent.hexsha] = (0, y_position)
        #             y_position -= 20
        #
        # # Create a plot with adjusted figure size
        # self.figure, self.ax = plt.subplots(figsize=(10, 10))
        #
        # nx.draw(self.graph, pos=positions, with_labels=False, node_size=50, node_color="skyblue", width=1)
        # nx.draw_networkx_labels(self.graph, pos=label_positions, labels={node: node for node in self.graph.nodes()}, font_size=7, ax=self.ax)
        #
        # # Adjust the x-axis limits to ensure labels are visible
        # self.ax.set_xlim([0, -10])
        #
        # # Adjust margins
        # plt.margins(.1)
        #
        # # Tight layout
        # plt.tight_layout()
        #
        # # Embed the plot in the panel
        # self.canvas = FigureCanvas(self, -1, self.figure)
        # self.canvas.SetSize((20, 20))
        #
        # # Horizontal sizer to split the panel
        # main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #
        # # Left section for graph visualization
        # self.canvas = FigureCanvas(self, -1, self.figure)  # Assuming you've created a figure for the graph
        # main_sizer.Add(self.canvas, 1, wx.EXPAND)
        #
        # # Right section for structured data view
        # self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)


        # sizer = wx.BoxSizer(wx.VERTICAL)
        # sizer.Add(self.canvas, 2, wx.EXPAND)
        # self.SetSizer(sizer)