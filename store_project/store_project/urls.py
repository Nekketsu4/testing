from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('store_app.urls')),
    path('admin/', admin.site.urls),
    path('capthca', include('captcha.urls')),
]
