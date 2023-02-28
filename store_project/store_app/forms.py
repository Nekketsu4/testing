from django.forms import ModelForm, formset_factory
from django import forms
from captcha.fields import CaptchaField

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


'''
Каптча связанная с моделью.
Объявляем поле типа CaptchaField предназначенный 
как раз для создания катптчи
'''
# class CaptchaModelForm(ModelForm):
#     captcha = CaptchaField()
#     class Meta:
#         model = Experiment


'''
Каптча НЕ связанная с моделью.
Объявляем поле типа CaptchaField предназначенный 
как раз для создания каптчи
'''
class CaptchatForm(forms.Form):
    captcha = CaptchaField(label='Вот эта строка будет вставлена'
                                 ' вместо слова Captcha')


'''Этот вариант каптчи выведет рандомный набор букв'''
# class CaptchaModelForm(ModelForm):
#     captcha = CaptchaField(generator='captcha.helpers.random_char_challenge')
#     class Meta:
#         model = Experiment


'''Этот вариант каптчи с вычеслением арифметического выражения
"надо решить просто пример"
'''
# class CaptchaModelForm(ModelForm):
#     captcha = CaptchaField(generator='captcha.helpers.math_challenge')
#     class Meta:
#         model = Experiment


'''
Этот вариант каптчи выдает рандомное слово которое должно
предверительно быть записано в словарь
'''
# class CaptchaModelForm(ModelForm):
#     captcha = CaptchaField(generator='captcha.helpers.word_challenge')
#     class Meta:
#         model = Experiment