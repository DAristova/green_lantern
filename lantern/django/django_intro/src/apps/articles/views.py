from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import SearchForm, ArticleForm
from .models import Article


def main_page(request):
    return render(request, 'pages/main_page.html')


def index(request):
    articles = Article.objects.all().values()
    return render(request, 'pages/article_list.html', {'articles': articles})


def articles_list_json(request):
    return JsonResponse(list(Article.objects.all().values()), safe=False)


def get_article_by_id(request, article_id):
    article_id = int(article_id)
    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return redirect('articles:index')
    return render(request, 'pages/view_article.html', {'article': article})


def upload(request):
    upload = ArticleForm()
    if request.method == 'POST':
        upload = ArticleForm(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect('articles:index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'articles:index'}}">reload</a>""")
    else:
        return render(request, 'pages/upload_form.html', {'upload_form': upload})


def update_article(request, article_id):
    article_id = int(article_id)
    try:
        article_sel = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return redirect('articles:index')
    art_form = ArticleForm(request.POST or None, instance=article_sel)
    if art_form.is_valid():
        art_form.save()
        return redirect('articles:index')
    return render(request, 'pages/upload_form.html', {'upload_form': art_form})


def delete_article(request, article_id):
    article_id = int(article_id)
    try:
        article_sel = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return redirect('articles:index')
    article_sel.delete()
    return redirect('articles:index')


class SearchResultsView(View):
    def get(self, request, **kwargs):
        # form = SearchForm(data=request.GET)
        search_q = request.GET.get('search', '')
        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()

        context_data = {
            'articles': articles,
            # 'search_form': form
        }
        return render(request, 'pages/search.html', context=context_data)