from django.shortcuts import render
from rest_framework import viewsets

from broadcasts.models import Client, Broadcast, Message
from broadcasts.serializers import ClientSerializer, BroadcastSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class BroadcastViewSet(viewsets.ModelViewSet):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

