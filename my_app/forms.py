from django import forms
from .models import Comment , Book


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'body', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kitob nomi'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Kitob tavsifi'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
