from rest_framework import serializers

from broadcasts.models import Client, Broadcast, Message


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class BroadcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcast
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'