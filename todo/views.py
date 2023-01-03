from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    #使用（操作）するモデルの指定を必ずやる
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    '''
    detailViewはurls.pyで任意のデータを指示しないといけない
    pk or slug
    '''
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel

    #表示する要素指定
    fields = ('title',"memo","priority","duedate")
    #登録成功時の遷移場所指定
    success_url = reverse_lazy("list")

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy("list")    
    '''
    deleteViewはurls.pyで任意のデータを指示しないといけない
    pk or slug
    '''

class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = TodoModel
    success_url = reverse_lazy("list")
    #表示する要素指定
    fields = ('title',"memo","priority","duedate")
    '''
    updateViewはurls.pyで任意のデータを指示しないといけない
    pk or slug
    '''
