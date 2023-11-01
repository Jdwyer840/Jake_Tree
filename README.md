if SourceTree == Meh:
    use_JakeTree = True
else:
    use_JakeTree = True

Lol

This is a for fun project mainly. Endeavoring into GUI with python and building a SourceTree type program that can hopefully simplify and make better, a lot of the features of source tree.

TODOS:
Get an understanding of the basics of wxPython and gitPython packages.
connect to a repository with the git package
figure out a way to display a git graph in the center of the console.
see if we can make a top task bar (file, edit, etc...)

features:
list out local branches on load
checkout branch


TODOs:
make current branch indicator good, update branch colors, maybe make a helper class for this
display commit history of a branch?
figure out how to make a panel scrollable
button color helper so that on clicks and on hovers dont change colors incorrectly and that when a branch is checked out and so another is no longer checked in, the colors are updated accordingly
figure out a way to display a chart or graph in the panel on a button click.

chatgpt's suggestions of what to do next: lol

Commit History Visualization: Consider using a tree or graph structure to visualize the commit history. This will give users a clear view of the commit lineage and branching. You can use libraries like networkx for the data structure and matplotlib for visualization, or integrate with other visualization tools.

Diff Viewer: Implement a diff viewer so that when a user clicks on a commit, they can see the changes made in that commit compared to its parent.

Repository Manager: As you mentioned, allowing users to add, remove, or switch between repositories would be a great feature. You can also add features like cloning a repo from a URL.

Error Handling: Ensure that you have robust error handling, especially when performing Git operations. For instance, if a branch has uncommitted changes and the user tries to switch branches, handle that scenario gracefully.

UI/UX Enhancements: Consider adding icons, tooltips, and other UI elements to make the application more intuitive. Also, think about keyboard shortcuts for common operations.

Performance: As the repository grows and the number of branches and commits increases, ensure that the application remains responsive. Consider lazy loading or pagination for large commit histories.

Documentation & Help: Provide a help section or documentation within the app to guide new users.

actually some good steps

organize project better... have a git widgets and settings widgets and shit like that!


git graph is still hard as fuck to build,

tool bar should have some more buttons and stuff

work on styling

the row fivew thing should have autor and date

try and get the top top file , options tool bar

figure out something to do with the theme manager... so that certain components can reset the themes for what they are?
like for instance checking out a branch should change the theme to the correct colors... we can sort of take a react appraoch to this
have each component decide what to do with their own theme...
maybe have a method in the theme manager that takes in a component as a param and will perform shit on it that way?


work on state of the application...