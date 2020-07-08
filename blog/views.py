from django.shortcuts import render
from django.views.generic import TemplateView, View


class HomePage(TemplateView):
    template_name = 'blog/index.html'
