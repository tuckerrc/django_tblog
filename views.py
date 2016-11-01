from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Post

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'tblog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'tblog/detail.html'
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())
