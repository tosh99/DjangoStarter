
from django.contrib import admin
from django.urls import path
import Engine.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
]
