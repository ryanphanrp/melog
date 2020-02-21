from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ListStoryView(ListView):
    model = Post
    template_name = 'story.html'


class CreatePostView(CreateView):
    model = Post
    fields = ['body']
    template_name = 'createpost.html'


class UpdatePostView(UpdateView):
    model = Post
    fields = ['body']
    template_name = 'editpost.html'


class DeletePostview(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('story')