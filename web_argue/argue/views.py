from django.views.generic import CreateView

from argue.models import Argue


class IndexView(CreateView):
    model = Argue
    template_name = 'argue/index.html'
    fields = ['title', 'text']
