from .models import EducationalMaterials, GiveBestAdvice
from django import forms

class EducationMaterialForm(forms.ModelForm):
    class Meta:
        model = EducationalMaterials
        fields = '__all__'


class GiveBestAdviceForm(forms.ModelForm):
    class Meta:
        model = GiveBestAdvice
        fields = '__all__'

