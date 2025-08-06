from django.urls import path, include
# from my_first_django_project.catalog.apps import CatalogConfig
# from my_first_django_project.catalog.views import home, contacts
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]