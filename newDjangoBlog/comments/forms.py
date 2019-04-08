from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment   #表单对应的数据库模型是Comment类
        fields = ['name', 'email', 'url', 'text']  #指定表单需要显示的字段



