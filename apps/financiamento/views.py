from django.shortcuts import render
from .forms import StepOneFinanciamento

def financiamento(request):

    form = StepOneFinanciamento

    if request.method == 'POST':
        form = StepOneFinanciamento(request.POST)

        if form.is_valid():
            return render(request, 'financiamento/financiamento.html')

    return render(request, 'financiamento/financiamento.html', {'form':form})
