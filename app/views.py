from django.shortcuts import render


def IndexView(request):
    return render(request=request,
                  template_name='app/index.html')


def PortfolioView(request):
    return render(request=request,
                  template_name='app/portfolio.html')
