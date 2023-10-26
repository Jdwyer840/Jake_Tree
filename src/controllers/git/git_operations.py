import git


class GitOperationConstants:
    LOCAL = "local"
    REMOTE = "remote"


class GitOperations:

    @staticmethod
    def get_current_local_branches(repo_path):
        print("getting current local branches")
        repo = git.Repo(repo_path)
        return {branch.name: branch for branch in repo.branches}

    @staticmethod
    def check_out_local_branch(repo_path: str, branch_name: str):
        #TODO find out a way o set the current repo use the new class repo manager
        repo = git.Repo(repo_path)
        repo.git.checkout(branch_name)
        print("")


    @staticmethod
    def is_branch_checked_out(repo_path: str, branch_name: str):
        repo = git.Repo(repo_path)
        return repo.active_branch.name == branch_name

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
