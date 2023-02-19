from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('store_app/', include('store_app.urls')),
    path('admin/', admin.site.urls),
    path('capthca', include('captcha.urls')),
]
