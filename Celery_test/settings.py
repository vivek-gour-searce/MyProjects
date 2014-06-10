__author__ = 'vivek.gour'

BROKER_URL = 'mongodb://127.0.0.1:27017/Test'

CELERY_RESULT_BACKEND = 'mongodb://127.0.0.1:27017:27017/'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'database': 'Test',
    'taskmeta_collection': 'testing',
}