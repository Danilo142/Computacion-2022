
from celery import Celery


app = Celery('celery_app', broker='amqp://guest@localhost//')

app.conf.update({
    'task_routes': {
        'celery_app.potencia': {'queue': 'potencia'},
        'celery_app.raiz': {'queue': 'raiz'},
        'celery_app.logaritmo': {'queue': 'logaritmo'},
    },
})
   
