from .celery import celery_app
from .funcs import *


@celery_app.task
def check_pending_related_issues():
    """
    Verifica issues relacionadas a PRs mergeados que ainda estão abertas
    """
    issues = repo.get_issues(state='open', labels=['ajuste pr'])
    pending_issues_texts = []

    for issue in issues:
        pr_data = re.search("#\d+", issue.body)
        if pr_data:
            pr_number = int(pr_data.group()[1:])
            pull_request = repo.get_pull(pr_number)
            if pull_request.merged:
                pending_issues_texts.append(f'A issue {issue.number} está relacionada ao PR {pull_request.number} que já foi mergeado.\nResponsável: {pull_request.user.login}')

    if pending_issues_texts:
        notify_related_issue_in_slack(pending_issues_texts)
