from rest_framework.response import Response
from rest_framework import viewsets
from Banco_digital.Models.nova_conta_models import nova_conta
from Banco_digital.Serializer.nova_conta_serializer import nova_contaSerializer

class nova_contaViewset(viewsets.ModelViewSet):
    queryset = nova_conta.objects.all()
    serializer_class = nova_contaSerializer