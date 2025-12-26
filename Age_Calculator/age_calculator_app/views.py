from django.shortcuts import render
from datetime import date
from .forms import AgeCalculatorForm

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def age_calculator_view(request):
    age = None
    if request.method == 'POST':
        form = AgeCalculatorForm(request.POST)
        if form.is_valid():
            birth_date = form.cleaned_data['date_of_birth']
            age = calculate_age(birth_date)
    else:
        form = AgeCalculatorForm()
    return render(request, 'age_calculator.html', {'form': form, 'age': age})