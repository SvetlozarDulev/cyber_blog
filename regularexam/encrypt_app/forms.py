from django import forms


class EncryptionForm(forms.Form):
    text = forms.CharField(max_length=200)
