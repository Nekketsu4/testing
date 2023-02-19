from django.forms import ModelForm, formset_factory
from django import forms

from .models import ListStore, RubricStore

class ListStoreForm(ModelForm):
    class Meta:
        model = ListStore
        fields = ('title', 'content', 'price', 'rubric')

class LookingForForm(forms.Form):
    keyword = forms.CharField(max_length=30, label='Напишите что ищете')
    rubric = forms.ModelChoiceField(queryset=RubricStore.objects.all(),
                                    label='Рубрика')


form_set = formset_factory(LookingForForm, extra=5, can_delete=True)

