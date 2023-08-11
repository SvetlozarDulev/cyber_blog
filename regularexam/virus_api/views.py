
import vt
from django.http import JsonResponse
from django.shortcuts import render

from .forms import ScanningLinkForm

def scan_url(request):
    if request.method == 'POST':
        form = ScanningLinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            api_key = 'YOUR_VIRUSTOTAL_API_KEY'  # Replace with your actual API key
            client = vt.Client(api_key)

            try:
                # Make the request to VirusTotal API
                link = client.get_object('/urls/{}', url)
                scan_result = {
                    'url': link.url,
                    'scan_date': link.scan_date,
                    'positives': link.positives,

                }
            except vt.APIError:
                scan_result = {
                    'error': 'There is no viruses in the link',
                }

            return render(request,'virus_result.html', scan_result)
    else:
        form = ScanningLinkForm()
    return render(request, 'scan_link.html', {'form':form})
