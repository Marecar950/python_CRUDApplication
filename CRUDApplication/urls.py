"""
URL configuration for CRUDApplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from client.views import create_client, update_client, delete_client, get_all_clients, get_clients_by_lastname, get_client_details_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clients', get_all_clients, name='get_all_clients'),
    path('api/clients/search/<str:client_lastname>', get_clients_by_lastname, name='get_clients_by_lastname'),
    path('api/client/<int:client_id>', get_client_details_by_id, name='get_client_details_by_id'),
    path('api/client/create', create_client, name='create-client'),
    path('api/client/update/<int:client_id>', update_client, name='update-client'),
    path('api/client/delete/<int:client_id>', delete_client, name='delete-client')
]
