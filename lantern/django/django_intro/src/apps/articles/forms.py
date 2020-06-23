from django import forms

from .models import Article


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'tags', 'author')
