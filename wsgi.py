from project import create_app
from .project.tasks import celery_app

application = create_app()



