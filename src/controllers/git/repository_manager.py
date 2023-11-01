#TODO this class will take care of what repo is checked out nd shit
import git


class GitRepositoryManager:
    """This class will be the selected repository tracker that git operations can use instead of
    cosntantly resue repo and repo pat
    """

    def __init__(self, repo_path: str):
        self.repo = None
        self.set_git_repository(repo_path=repo_path)

    def set_git_repository(self, repo_path: str) -> None:
        try:
            self.repo = git.Repo(path=repo_path)
        except git.InvalidGitRepositoryError as re:
            print(f"git repo is not good son {str(re)}")
            raise re

    def get_git_repository(self):
        return self.repo
