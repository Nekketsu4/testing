from django.forms import ModelForm

from .models import ListStore

class ListStoreForm(ModelForm):
    class Meta:
        model = ListStore
        fields = ('title', 'content', 'price', 'rubric')