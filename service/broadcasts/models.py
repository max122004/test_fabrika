from django.db import models


class Client(models.Model):
    number_phone = models.CharField(max_length=12, unique=True)
    operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Client: {self.number_phone} - {self.operator_code}'


class Broadcast(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    message = models.CharField(max_length=255)
    operator_code_filter = models.CharField(max_length=10)
    tag_filter = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'Broadcast: {self.message} ({self.start_time} - {self.end_time})'


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE, related_name='broadcasts')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'Message: {self.status} - {self.client}'
