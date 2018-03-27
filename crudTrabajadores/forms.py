from django import forms
from .models import Trabajador

class FormTrabajador(forms.ModelForm):

    class Meta:
        model = Trabajador
        fields = ('nombre','apellido','dni','telefono','cargo',)
