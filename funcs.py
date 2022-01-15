from github import Github
from .constants import *

# using an access token
g = Github(ACCESS_TOKEN)
repo = g.get_repo(PROJECT_TO_TRACK)

def check_pr_branch_is_correct(request_data):
    """
    Check if branch destination of PR in webhook is same of BRANCH_TO_TRACK

    - request_data [dict]: body of request to API
    """
    return request_data['pull_request']['base']['ref'] == BRANCH_TO_TRACK
    

def check_not_mergeable_prs():
    """
    Search for PRs with conflicts
    """
    not_mergeable_prs = []

    pulls = repo.get_pulls(state='open', sort='created', base=BRANCH_TO_TRACK)
    for pr in pulls:
        pr_detail = repo.get_pull(pr.number)
        if not pr_detail.mergeable: not_mergeable_prs.append(pr.number)

    return not_mergeable_prs

    
