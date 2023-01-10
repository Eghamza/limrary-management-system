from django.forms import ModelForm
from django import forms
from library_m_s.models import student
from django.contrib.auth.models import Group
class groupForm(ModelForm):
    class Meta:
        model = Group
        fields = ('__all__')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'Group.Permissions.name': forms.TextInput(attrs={'class': 'form-control'}),
                   }
