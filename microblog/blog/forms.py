from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta: #ModelFormの形式
        model = Comment #編集したいモデル名
        fields = ["name", "email", "body"] # 表示するフィールド名