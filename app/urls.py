from django.urls import path

from app.views import IndexView

urlpatterns = [
    path('', IndexView, name='index')
]