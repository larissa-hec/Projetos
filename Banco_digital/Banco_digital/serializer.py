from rest_framework import serializers
from Banco_digital.models import cliente


class clienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = cliente
        fields = "__all__"