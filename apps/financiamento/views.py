from django.shortcuts import render

def financiamento(request):
    return render(request, 'financiamento/financiamento.html')
