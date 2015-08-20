from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# get list Blog
def blog_list(request):
   # posts = Post.;
   # context = {'posts': posts}
    return render(request, 'blog/blog_list.html', {})
    