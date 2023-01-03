from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    #指定されているurlの場合todo.urlsを呼び出し
    path("",include("todo.urls")),
]
