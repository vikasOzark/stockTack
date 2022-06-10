from pydoc import render_doc
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .news import  get_headlines


# Create your views here.

class IndexHomeView(View):
    template_name = 'index.html'
    headlines_get = get_headlines()
    headlines = headlines_get['articles'][0]
    headlines2 = headlines_get['articles'][1]
    def get(self, request):
        return render(request, self.template_name, {'headlines' : self.headlines,
                                                        'headlines2' : self.headlines2})
