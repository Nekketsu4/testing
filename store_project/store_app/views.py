from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView


from .models import ListStore, RubricStore
from .forms import ListStoreForm, LookingForForm, formset_factory

# def index(request):
#     '''
#     метод defer наоборот разделит цельный sql-запрос записи
#     на два отдельных. Спервы выполнится запрос информации без поля price
#     затем поле price будет получено в отдельном запросе
#     '''
#     goods = ListStore.objects.defer('price').all()
#     rubrics = RubricStore.objects.all()
#     context = {'goods': goods, 'rubrics': rubrics}
#     return render(request, 'store_app/index.html', context)

def index(request):
    goods = ListStore.objects.all()
    rubrics = RubricStore.objects.all()
    context = {'goods': goods, 'rubrics': rubrics}
    return render(request, 'store_app/index.html', context)

# def check_rubric(request, check_rubric_id):
#     '''
#     этот вариант запросы более энергозатратный так как просит доп sql запрос
#     goods = ListStore.objects.filter(rubric=check_rubric_id)
#     тот что в коде напрямую обращается к первичной модели
#     '''
#     goods = ListStore.objects.select_related('rubric').filter(rubric=check_rubric_id)
#     rubrics = RubricStore.objects.all()
#     curr_rub = RubricStore.objects.get(pk=check_rubric_id)
#     context = {'goods': goods, 'rubrics': rubrics, 'curr_rub': curr_rub}
#     return render(request, 'store_app/check_rubric.html', context)

def check_rubric(request, rub_id):
    goods = ListStore.objects.filter(rubric=rub_id)
    rubrics = RubricStore.objects.all()
    curr_rub = RubricStore.objects.get(pk=rub_id)
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


def looking_for():
    if request.method == 'POST':
        look_for = LookingForForm(request.POST)
        if look_for.is_valid():
            keyword = look_for.cleaned_data['keyword']
            rubric_id = look_for.cleaned_data['rubric'].pk
            goods = ListStore.objects.filter(title__icontains=keyword,
                                             rubric=rubric_id)
            context = {'goods': goods}
            return render(request, 'store_app/looking_goods.html', context)
    else:
        look_for = LookingForForm()
        context = {'form': look_for}
        return render(request, 'store_app/looking_form')


def form_set_it(request):
    test_form = formset_factory(LookingForForm, extra=5, can_order=True,
                                can_delete=True)
    if request.method == 'POST':
        formset = test_form(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data and form.cleaned_data['DELETE']:
                    keyword = form.cleaned_data['keyword']
                    rubric_id = form.cleaned_data['rubric'].pk
                    order = form.cleaned_data['ORDER']
            return render(request, 'store_app/formset_res.html')
    else:
        formset = test_form()
    context = {'formset': formset}
    return render(request, 'store_app/formset.html', context)
