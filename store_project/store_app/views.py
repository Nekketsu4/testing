from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import ListStore, RubricStore
from .forms import  ListStoreForm

def index(request):
    goods = ListStore.objects.all()
    rubrics = RubricStore.objects.all()
    context = {'goods': goods, 'rubrics': rubrics}
    return render(request, 'store_app/index.html', context)

def check_rubric(request, check_rubric_id):
    goods = ListStore.objects.filter(rubric=check_rubric_id)
    rubrics = RubricStore.objects.all()
    curr_rub = RubricStore.objects.get(pk=check_rubric_id)
    context = {'goods': goods, 'rubrics': rubrics, 'curr_rub': curr_rub}
    return render(request, 'store_app/check_rubric.html', context)

class ListStoreCreateView(CreateView):
    template_name = 'store_app/store_create.html'
    form_class = ListStoreForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = RubricStore.objects.all()
        return context