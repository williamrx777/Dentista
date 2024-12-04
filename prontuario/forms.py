from django import forms
from .models import Prontuario

class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'inicio_tratamento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'termino_tratamento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'interrupcao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'tc': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'ts': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProntuarioForm, self).__init__(*args, **kwargs)
        self.fields['anotações'].required = False
        self.fields['sensibilidade_anestisia'].required = False
        self.fields['tratamento_realidado'].required = False
        for field_name, field in self.fields.items():
            if field_name not in self.Meta.widgets:  # Evita sobrescrever widgets personalizados
                field.widget.attrs['class'] = 'form-control'