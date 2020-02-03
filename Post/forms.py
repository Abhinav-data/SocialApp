from django import forms
from .models import UserPOST

class UserFormModelPost(forms.ModelForm):
    class Meta:
        model=UserPOST
        fields='__all__'
        exclude=('user',)
