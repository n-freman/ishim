from django import forms
from .models import Vacancy


class VacancyCreateForm(forms.ModelForm):
    
    class Meta:
        model = Vacancy
        fields = [
            'position', 
            'sphere',
            'min_salary',
            'max_salary',
            'registration',
            'experience',
            'min_age',
            'max_age',
            'sex',
            'education',
            'responsibilities',
            'work_terms',
            'busyness',
            'work_graph',
            'payment',
        ]