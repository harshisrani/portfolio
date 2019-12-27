#!/bin/sh

cd /code/ 
# run Celery worker with unpriviledged user for our myportfolio project with Celery configuration stored in celeryconf
celery --app=myportfolio.celeryconf worker --loglevel=info --concurrency=10 -n worker1.%h

# Production: run with unpriviledge user
# su -m celery-user -c "celery worker -A myportfolio.celeryconf -n worker1.%h"
