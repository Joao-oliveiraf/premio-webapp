from django.shortcuts import render,redirect
from .forms import StepOneFinanciamento,StepTwoFinanciamento_cpf,StepTwoFinanciamento_cnpj,StepThreeFinanciamento
from formtools.wizard.views import SessionWizardView
from django.contrib import messages

def financiamento(request):

    form = StepOneFinanciamento

    if request.method == 'POST':
        form = StepOneFinanciamento(request.POST)

        if form.is_valid():
            return render(request, 'financiamento/financiamento.html')

    return render(request, 'financiamento/financiamento.html', {'form':form})

def show_cpf_form(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    if cleaned_data.get('tipo_pessoa') == 'cpf':
        return True
    
def show_cnpj_form(wizard):
    cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
    if cleaned_data.get('tipo_pessoa') == 'cnpj':
        return True    
class WizardFinanciamentoForm(SessionWizardView):
    template_name = 'financiamento.html'
    form_list = [StepOneFinanciamento, StepTwoFinanciamento_cpf, StepTwoFinanciamento_cnpj]
    condition_dict = {'1': show_cpf_form,
                      '2': show_cnpj_form}

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        messages.success(self.request, 'Formulário enviado com sucesso!')
        return redirect('index')
