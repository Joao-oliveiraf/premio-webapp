from django.urls import path
from .views import financiamento, WizardFinanciamentoForm

urlpatterns = [
    path('financiamento', WizardFinanciamentoForm.as_view() , name='financiamento')
]