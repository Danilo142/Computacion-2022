from celery_app import app
from math import sqrt, log10

@app.task
def potencia(n):
    return n**2

@app.task
def raiz(n):
    return sqrt(n)

@app.task
def logaritmo(n):
    return log10(n)
