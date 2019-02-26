from django.contrib import admin
from django.urls import path
import Engine.views as v

urlpatterns = [
    path('api', v.resolveapi),
    path('admin/', admin.site.urls),
]
