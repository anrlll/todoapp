from django.contrib import admin
from .models import TodoModel
# Register your models here. 

#管理画面にTodomodelsを表示
admin.site.register(TodoModel)
