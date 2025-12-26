from django import forms

class AgeCalculatorForm(forms.Form):
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'type': 'date',
        }))