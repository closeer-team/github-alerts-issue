from flask import request, Response, Blueprint
from .check_signature import verify_signature
from .funcs import get_related_issue, notify_related_issue_in_slack
import json

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/check_pending_issues', methods=['POST',])
def check_prs():
    signature_256 = request.headers['X-Hub-Signature-256']
    if not verify_signature(signature_256, request.data):
        return Response(status=403)

    pr_data = json.loads(request.data)

    related_issue = get_related_issue(pr_data['number'])
    if related_issue:
        notify_related_issue_in_slack(
            related_issue,
            pr_data['pull_request']['user']['login'],
            pr_data['number']
        )

    return Response(status=200)


