from django.urls import path

from app.views import IndexView, PortfolioView

urlpatterns = [
    path('', IndexView, name='index'),
    path('portfolio/', PortfolioView, name='portfolio')
]