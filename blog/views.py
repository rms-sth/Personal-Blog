from django.shortcuts import render
from django.views.generic import TemplateView, View


class HomePage(TemplateView):
    template_name = 'blog/index.html'


class BlogDetailView(TemplateView):
    template_name = 'blog/blog_detail.html'


class AboutView(TemplateView):
    template_name = 'blog/about.html'