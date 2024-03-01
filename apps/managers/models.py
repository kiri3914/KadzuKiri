from django.db import models

class Department(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title

class Managers(models.Model):
    POSITION_CHOICES = (
        ('Manager', 'Менеджер'),
        ('Assistant Manager', 'Помощник управляющего'),
        ('Assistant', 'Ассистент'),
        ('Secretary', 'Секретарь'),
        ('Accountant', 'Бухгалтер'),
        ('Director', 'Директор'),
        ('Head', 'Главный менеджер'),
        ('Supervisor', 'Начальник'),
    )
    id = models.OneToOneField(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    contact_number = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='managers')


    def __str__(self):
        return self.id

