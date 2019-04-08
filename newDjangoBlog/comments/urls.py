from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name='comments' #指定命名空间，防止和其他应用的name冲突
urlpatterns = [
    path('comment/post/<int:post_pk>', views.post_comment, name='post_comment'),

]