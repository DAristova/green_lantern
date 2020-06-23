from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-article'),
    path('<int:article_id>', views.get_article_by_id),
    path('update/<int:article_id>', views.update_article),
    path('delete/<int:article_id>', views.delete_article),
    path('search/', views.main_page, name='main-page'),
    path('results/', views.SearchResultsView.as_view(), name='search-results')
]
