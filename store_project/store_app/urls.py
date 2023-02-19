from django.urls import path

from .views import index, check_rubric, ListStoreCreateView

app_name = 'liststore'

urlpatterns = [
    path('add/', ListStoreCreateView.as_view(), name='add'),
    path('<int:check_rubric_id>/', check_rubric, name='check_rubric'),
    path('', index, name='index')
]

