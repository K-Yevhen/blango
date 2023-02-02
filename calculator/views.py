from django.shortcuts import render, redirect
from .forms import CalculatorForm

# Create your views here.

def calculate(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            first_number = form.cleaned_data['first_number']
            second_number = form.cleaned_data['second_number']
            operation = form.cleaned_data['operation']
            result = None
            if operation == 'add':
                result = first_number + second_number
            elif operation == 'sub':
                result = first_number - second_number
            elif operation == 'mul':
                result = first_number * second_number
            elif operation == 'div':
                result = first_number / second_number
            return render(request, 'calculator/result.html', {'result': result})
    else:
        form = CalculatorForm()
    return render(request, 'calculator/calculate.html', {'form': form})
