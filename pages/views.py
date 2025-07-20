from django.http import HttpResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'home.html'


def homePageView(request) -> HttpResponse:
  return HttpResponse('Hello, World')


class AboutPageView(TemplateView):
  template_name = 'about.html'