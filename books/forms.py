from django import forms
from .models import Book, Comment


class Book_Form(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title','author','genre','content','image')
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'title'
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'author'
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'genre'
                }
            ),
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'content',
                }
            ),
        }
    
class Comment_Form(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('user','book',)
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'content',
                }
            ),
            'rank': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '0 ~ 5'
                }
            ),
        }