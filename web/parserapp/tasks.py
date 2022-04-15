import logging
from celery import shared_task
from .src.get_data import create_records_db


@shared_task
def background_finding_data_from_remote_api(url):
    result = create_records_db(url)
    logging.warning(result)
