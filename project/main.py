from flask import request, Response, Blueprint
from .check_signature import verify_signature
from .funcs import get_related_issue, notify_related_issue_in_slack, pr_is_merged
import json

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/check_pending_issues', methods=['POST',])
def check_prs():
    signature_256 = request.headers['X-Hub-Signature-256']
    if not verify_signature(signature_256, request.data):
        return Response(status=403)

    pr_data = json.loads(request.data)

    if not pr_is_merged(pr_data['number']):
        return Response(status=200)

    related_issue = get_related_issue(pr_data['number'])
    if related_issue:
        notify_related_issue_in_slack(
            f"A issue {related_issue} está relacionada ao PR {pr_data['number']} que acabou de ser mergeado.\nResponsável: {pr_data['pull_request']['user']['login']}"
        )

    return Response(status=200)


