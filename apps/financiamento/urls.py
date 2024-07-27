from django.urls import path
from .views import financiamento

urlpatterns = [
    path('financiamento', financiamento, name='financiamento')
]