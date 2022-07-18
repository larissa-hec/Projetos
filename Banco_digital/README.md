Instalação Django

Projeto

*Ambiente virtual do python
python3 -m venv .venv

*Ativação ambiente virtual Linux
source .venv/bin/activate

*Ativação ambiente virtual Windows
.venv\Scripts\activate.bat

*Instalação django
pip install django

*criação projeto
django-admin startproject conta .
configurações de idioma. no arquivo configuracoes/settings.py altere as constantes

LANGUAGE_CODE = 'pt-br' 
TIME_ZONE = 'America/Sao_Paulo'

*criar um novo app
python manage.py startapp Banco_digital .

*Instalação do MySQLClient
pip install mysqlclient

*Instalação Djangorestframework
pip install djangorestframework
pip install markdown
pip install django-filter 

*Configuração
No arquivo configuracoes/settings.py adicionar o 'rest_framework' aos APPS

INSTALLED_APPS = [
    ...
    'rest_framework',
    'Banco_digital',
]

*no arquivo configuracoes/urls.py

...
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    ...
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

Paginação
Adicione as seguintes linhas configuracoes/settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
