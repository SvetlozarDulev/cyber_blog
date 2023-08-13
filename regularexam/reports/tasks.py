from celery import shared_task
import time

@shared_task
def fetch_cybersecurity_news():
    #Simulate asynchronous task
    time.sleep(5)

    news = [
        'Police seize LOLEK bulletproof service for hosting malware',
        'Lapsus$ hackers took SIM-swapping attacks to the next level',
        'New BitForge cryptocurrency wallet flaws lets hackers steal crypto',
    ]
    return news