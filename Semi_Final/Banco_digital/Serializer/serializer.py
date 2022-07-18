from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from contas.models import cliente


class clienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = cliente
        fields = "__all__"