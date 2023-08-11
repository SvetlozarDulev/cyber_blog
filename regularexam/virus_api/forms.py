from django import forms
from .models import ScanningLink

class ScanningLinkForm(forms.ModelForm):
    class Meta:
        model = ScanningLink
        fields = '__all__'