from github import Github
from .constants import *
import requests
import json
import re

# using an access token
g = Github(ACCESS_TOKEN)
repo = g.get_repo(PROJECT_TO_TRACK)


def pr_is_merged(pr_id: int):
    """
    Verifica se o Pull Request já foi mergeado
    """
    pull_request = repo.get_pull(pr_id)
    return pull_request.merged


def get_related_issue(pr_id: int):
    """
    Retorna a issue relacionada ao PR

    - pr_id [int]: ID do PR a ser verificado

    """
    pr_id = str(pr_id)
    issues = repo.get_issues(state='open', labels=['ajuste pr'])
    related_issue = None

    for issue in issues:
        pr_data = re.search("#\d+", issue.body)
        if pr_data and pr_id in pr_data.group():
            related_issue = issue.number
            break

    return related_issue


def notify_related_issue_in_slack(texts: list):
    """
    Envia a notificação de issue relacionada ao PR para o slack

    - issue_id [int]: ID da issue relacionada
    - user_login [str]: Nome de usuário do responsável pelo PR
    - pr_id [int]: ID do Pull Request
    """
    data = {
        'text': '\n\n'.join(texts)
    }

    requests.post(SLACK_WEBHOOK_LINK, data=json.dumps(data))

# alterar para ser uma task que verifica periodicamente todos os PRs
