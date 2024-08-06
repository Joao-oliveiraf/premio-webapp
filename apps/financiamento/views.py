from django.shortcuts import render
from .forms import StepOneFinanciamento,StepTwoFinanciamento,StepThreeFinanciamento
from formtools.wizard.views import SessionWizardView

def financiamento(request):

    form = StepOneFinanciamento

    if request.method == 'POST':
        form = StepOneFinanciamento(request.POST)

        if form.is_valid():
            return render(request, 'financiamento/financiamento.html')

    return render(request, 'financiamento/financiamento.html', {'form':form})

class WizardFinanciamentoForm(SessionWizardView):
    template_name = 'financiamento.html'
    form_list = [StepOneFinanciamento, StepTwoFinanciamento]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })
