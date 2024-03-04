import os
from celery import Celery

# Установите модуль настроек Django по умолчанию для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Используя строка здесь означает, что рабочему не нужно сериализовать
# объект конфигурации дочерним процессам.
# - namespace='CELERY' означает, что все связанные с сельдереем ключи конфигурации
# должны иметь префикс `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузить модули задач из всех зарегистрированных приложений Django.
app.autodiscover_tasks ()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Запрос: {self.запрос!r}')