from django.shortcuts import render
from cryptography.fernet import Fernet
from .forms import EncryptionForm


def encryption(request):
    form = EncryptionForm()
    key = Fernet.generate_key()
    fernet = Fernet(key)

    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text'].encode()
            encrypted_text = fernet.encrypt(text)
            context['encrypted_text'] = encrypted_text
            context['key'] = key
            context['decrypted_text'] = fernet.decrypt(encrypted_text)

    return render(request, 'encryption_template.html', context)



