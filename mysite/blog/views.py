from django.shortcuts import render
from django.views.generic import (TemplateView,ListView)
from blog.models import *
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post


    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

        #from get_queryset we are going to do a query like a sql query-
        #we are basically saying grab the post model and filter out based on the given conditions
        