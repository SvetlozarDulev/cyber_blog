from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView
from .forms import EducationMaterialForm
from django.urls import reverse_lazy
from .models import EducationalMaterials, GiveBestAdvice
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class EducationView(LoginRequiredMixin, CreateView):
    model = EducationalMaterials
    template_name = 'education_materials.html'
    fields = ('title','description','url')


class EducationList(ListView):
    template_name = 'education_materials_list.html'
    model = EducationalMaterials

class GiveBestAdviceView(LoginRequiredMixin,CreateView):
    model = GiveBestAdvice
    template_name = 'give_best_advice.html'
    fields = (
        'text',
    )

class AdvicesList(ListView):
    template_name = 'advice_list.html'
    model = GiveBestAdvice
