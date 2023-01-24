from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'calculator/index.html'
    context_object_name = 'number'

    def get_queryset(self):
        pass
