import git
# from repository_manager import GitRepositoryManager


class GitOperationConstants:
    LOCAL = "local"
    REMOTE = "remote"


class GitOperations:
    repo: git.Repo = None

    def __init__(self, repo_path: str):
        self.set_git_repository(repo_path)

    def set_git_repository(self, repo_path: str) -> None:
        try:
            self.repo = git.Repo(path=repo_path)
        except git.InvalidGitRepositoryError as re:
            print(f"git repo is not good son {str(re)}")
            raise re

    def get_git_repository(self):
        return self.repo

    @staticmethod
    def get_current_local_branches(repo_path):
        print("getting current local branches")
        repo = git.Repo(repo_path)
        return {branch.name: branch for branch in repo.branches}

    @staticmethod
    def check_out_local_branch(repo_path: str, branch_name: str):
        #TODO find out a way o set the current repo use the new class repo manager
        repo = git.Repo(repo_path)
        # repo.
        repo.git.checkout(branch_name)
        print("")

    @staticmethod
    def get_commit_history(repo_path: str):
        #TODO find out a way o set the current repo use the new class repo manager
        repo = git.Repo(repo_path)
        branch_name = GitOperations.get_current_branch_name(repo_path)
        return list(repo.iter_commits(branch_name, max_count=50))
        # repo.
        # repo.git.checkout(branch_name)
        # print("")

    @staticmethod
    def get_current_branch_name(repo_path: str = None):
        repo_path = repo_path if repo_path else r'C:\Users\jacob\Documents\ETE\repos\ete-sync-internal'
        repo = git.Repo(repo_path)
        return repo.active_branch.name

    @staticmethod
    def is_branch_checked_out(repo_path: str, branch_name: str):
        repo = git.Repo(repo_path)
        return repo.active_branch.name == branch_name

    def get_branches_grouped_by_prefix_dict(self):
        no_prefix = "no_prefix"
        grouped_branches = {no_prefix: []}
        for branch in self.repo.branches: # noqa
            if "/" in branch.name:
                branch_prefix, branch_name = branch.name.split("/", 1)
                if branch_prefix not in grouped_branches:
                    grouped_branches[branch_prefix] = []
                grouped_branches[branch_prefix].append(branch_name)
            else:
                grouped_branches[no_prefix].append(branch.name)
        return grouped_branches




    @staticmethod
    def get_current_remote_branches(repo_path):
        repo = git.Repo(repo_path)
        git_remote_obj = {}
        for remote in repo.remotes:
            for ref in remote.refs:
                git_remote_obj[f"{ref.name}"] = ref
        return git_remote_obj

    @staticmethod
    def _get_current_branches(branch_type: str = GitOperationConstants.LOCAL):
        #
        print("getting branches")
        # current_branches = git.

    @staticmethod
    def get_repo_info(path: str) -> dict:
        try:
            # Try to initialize a Repo object. If the path isn't a repo, this will raise an exception.
            repo = git.Repo(path)

            # If no exception was raised, gather some basic info.
            info = {
                'is_repo': True,
                'active_branch': repo.active_branch.name,
                'latest_commit': repo.head.commit.hexsha,
                'latest_commit_message': repo.head.commit.message,
                'remote_url': next(repo.remote().urls) if repo.remotes else None  # Get the URL of the first remote, if any.
            }
            return info

        except git.InvalidGitRepositoryError:
            # The path is not a valid git repository.
            return {
                'is_repo': False
            }
