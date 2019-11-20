from django.shortcuts import render
from django.utils import timezone

from .models import ClassBlog
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class BlogView(ListView): 
    #html템플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html
    
    #template_name = 'classcrud/list.html' -> 템플릿 디폴트 파일 이름 변경
    #context_object_name = 'blog_list' -> 오브젝트 이름 변경
    model = ClassBlog

class BlogCreate(CreateView): #html : form(입력 공간)을 갖고있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list') #redirection

class BlogDetail(DetailView):
    model = ClassBlog #html :상세페이지를 담은 html : (소문자 모델)_detail.html
    
    
class BlogUpdate(UpdateView): # html : form(입력공간)을  갖고있는 html
    model = ClassBlog        #      (소문자 모델)_form.html 
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):       #html : "이거 진짜 지울거야?" (소문자모델)_confirm_delete.html
    model = ClassBlog       
    success_url = reverse_lazy('list')
