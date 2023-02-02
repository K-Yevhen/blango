from django import forms

class CalculatorForm(forms.Form):
    first_number = forms.FloatField()
    second_number = forms.FloatField()
    operation = forms.ChoiceField(choices=[('add', '+'), ('sub', '-'), ('mul', '*'), ('div', '/')])
