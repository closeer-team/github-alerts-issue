from celery import Celery
from .constants import REDIS_URL

celery_app = Celery('tasks', broker=REDIS_URL)
celery_app.conf.update(
    enable_utc=True,
    timezone='America/Fortaleza',
)

# agendando a task periódica
celery_app.conf.beat_schedule = {
    'notify-pending-issues': {
        'task': 'project.tasks.check_pending_related_issues',
        'schedule': 10.0,
    },
}

