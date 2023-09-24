import requests
from celery import shared_task
from celery_singleton import Singleton

from django.utils import timezone

from broadcasts.models import Broadcast, Client, Message

YOUR_JWT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjU3MDA1MzcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9yYXp3NjcifQ.YWLBAkXqWz1NPd0kavR2-wb6GmrMkHfNXpy4hcgIrVg'


@shared_task(base=Singleton)
def process_broadcast(broadcast_id):
    try:
        broadcast = Broadcast.objects.get(pk=broadcast_id)

        current_time = timezone.now()
        if broadcast.start_time <= current_time < broadcast.end_time:
            clients = Client.objects.filter(
                operator_code='beeline',
                tag='beeline'
            )

            for client in clients:
                message = Message.objects.create(
                    status='Pending',
                    broadcast=broadcast,
                    client=client
                )

                response = send_message_to_external_service(client.phone_number, broadcast.message)

                if response.status_code == 200:
                    message.status = 'Sent'
                else:
                    message.status = 'Failed'

                message.save()

            broadcast.status = 'Completed'
            broadcast.save()

    except Broadcast.DoesNotExist:
        pass


def send_message_to_external_service(phone_number, message):
    headers = {
        'Authorization': f'Bearer {YOUR_JWT_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'id': 0,
        'phone': phone_number,
        'text': message,
    }

    url = 'https://probe.fbrq.cloud/v1/send/1'

    response = requests.post(url, headers=headers, json=data)

    return response
