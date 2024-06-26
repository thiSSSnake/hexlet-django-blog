# hexlet_django_blog/views.py
from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView


# class HomePageView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['who'] = 'World'
#         return context


def index(request):
    return render(request, 'base.html')


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
        )