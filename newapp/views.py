from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from core.models import Question

class Home(TemplateView):
    template_name = "index.html"


class SecondPage(TemplateView):
    template_name = "index2.html"

class CreatePage(CreateView):
    template_name = "index2.html"
    model = Question
    success_url = "/list"
    fields = ['question_text','first_name', 'last_name']

class ListPage(ListView):
    template_name = "list.html"
    model = Question
